import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
import json
import subprocess
import sys
import tempfile

PATH=Path(__file__).resolve().parents[1]/'scripts/reference_tools.py'
spec=importlib.util.spec_from_file_location('references',PATH)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class ReferenceTools(unittest.TestCase):
    def setUp(self):
        self.paper={'doi':'10.1234/example','title':'GPU Scheduling: A Study','authors':['Alice Lin','Bo Wu'],'year':2024,'venue':'Example Conference'}
    def test_doi_normalization(self):
        self.assertEqual(m.normalize_doi('https://doi.org/10.1234/ABC'),'10.1234/abc')
        with self.assertRaises(ValueError):m.normalize_doi('https://example.org/a')
    def test_same_doi_wrong_title(self):
        observed=dict(self.paper,title='Unrelated Storage Method')
        self.assertEqual(m.compare(self.paper,observed)['status'],'needs_review')
    def test_author_order(self):
        observed=dict(self.paper,authors=['Bo Wu','Alice Lin'])
        self.assertEqual(m.compare(self.paper,observed)['checks']['authors'],'review')
    def test_metadata_match_separate_from_support(self):
        result=m.compare(self.paper,self.paper)
        self.assertEqual(result['status'],'metadata_match')
        self.assertEqual(result['claim_support'],'requires_reading')
    def test_missing_fields_are_partial(self):
        self.assertEqual(m.compare({'doi':self.paper['doi']},self.paper)['status'],'metadata_partial')
    def test_error_is_unresolved(self):
        with patch.object(m,'lookup',side_effect=OSError('timeout')):
            self.assertEqual(m.verify(self.paper)['status'],'unresolved')
    def test_title_only_remains_candidate(self):
        with patch.object(m,'search',return_value={'papers':[self.paper]}):
            self.assertEqual(m.verify({'title':self.paper['title']})['status'],'needs_identifier')
    def test_no_bibtex_generation_after_error(self):
        with patch.object(m,'fetch',side_effect=OSError('timeout')):
            with self.assertRaises(OSError):m.bibtex(self.paper['doi'])
    def test_html_is_not_bibtex(self):
        with patch.object(m,'fetch',return_value='<html>Login</html>'):
            with self.assertRaises(ValueError):m.bibtex(self.paper['doi'])
    def test_retrieved_entry_preserved(self):
        raw='@article{x, title={GPU}, author={Lin, Alice and Wu, Bo}}'
        with patch.object(m,'fetch',return_value=raw):
            self.assertEqual(m.bibtex(self.paper['doi'])['bibtex'],raw)
    def test_official_bibtex_fallback(self):
        raw='@article{x, title={GPU}}'
        with patch.object(m,'fetch',side_effect=[OSError('429'),raw]) as fetch:
            result=m.bibtex(self.paper['doi'])
            self.assertEqual(result['bibtex'],raw)
            self.assertIn('api.crossref.org',result['bibtex_source'])
            self.assertEqual(fetch.call_count,2)
    def test_title_lookup_error_is_unresolved(self):
        with patch.object(m,'search',side_effect=OSError('timeout')):
            self.assertEqual(m.verify({'title':'GPU'})['status'],'unresolved')
    def test_links_encoded_and_no_network(self):
        with patch.object(m,'fetch',side_effect=AssertionError('network')):
            result=m.search_links('GPU & latency',['OSDI'])
        self.assertIn('%26',result['global']['dblp'])
        self.assertIn('OSDI',result['per_venue'][0]['dblp'])
    def test_group_author_and_order(self):
        item={'title':['A'],'author':[{'name':'Research Group'},{'given':'Bo','family':'Wu'}]}
        self.assertEqual(m.record(item)['authors'],['Research Group','Bo Wu'])
    def test_cli_input_is_read_only(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'input.json';p.write_text('[{}]');before=p.read_bytes()
            out=subprocess.run([sys.executable,str(PATH),'verify','--input',str(p)],capture_output=True,text=True)
            self.assertEqual(out.returncode,0)
            self.assertEqual(json.loads(out.stdout)[0]['verification']['status'],'needs_identifier')
            self.assertEqual(before,p.read_bytes())
    def test_malformed_cli(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'input.json';p.write_text('{"papers":null}')
            out=subprocess.run([sys.executable,str(PATH),'verify','--input',str(p)],capture_output=True)
            self.assertEqual(out.returncode,2)

if __name__=='__main__':unittest.main()

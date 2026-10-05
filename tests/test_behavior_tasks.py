import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('behavior', ROOT / 'scripts/behavior_eval.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class EngineeringFixtures(unittest.TestCase):
    def test_blind_inputs_and_recording(self):
        with tempfile.TemporaryDirectory() as tmp:
            for task in json.loads((ROOT / 'tests/behavior/tasks.json').read_text()):
                dest = m.prepare(task, Path(tmp) / task, 'current')
                self.assertFalse((dest / 'skill/tests').exists())
                self.assertFalse((dest / 'skill/examples').exists())
                self.assertFalse((dest / 'skill/validation').exists())
                self.assertEqual(json.loads((dest / 'manifest.json').read_text())['status'], 'prepared_not_run')
                with self.assertRaises(ValueError):
                    m.record(dest, 'test', 'test', ['file-read'])
                with self.assertRaises(ValueError):
                    m.prepare(task, dest, 'current')
            self.assertTrue((Path(tmp) / 'entrusted/materials/sealed-manuscript.md').exists())

    def test_patch_applies_and_protects_unrelated_semantics(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'paper'; shutil.copytree(ROOT / 'examples/paper', dest)
            before = {str(p.relative_to(dest)): p.read_bytes() for p in dest.rglob('*') if p.is_file()}
            patch = ROOT / 'examples/author-revision.diff'
            result = subprocess.run(['git', 'apply', '--check', str(patch)], cwd=dest, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            subprocess.run(['git', 'apply', str(patch)], cwd=dest, check=True)
            allowed = {'sections/abstract.tex', 'sections/introduction.tex', 'sections/design.tex', 'sections/evaluation.tex'}
            for name, data in before.items():
                if name not in allowed:
                    self.assertEqual((dest / name).read_bytes(), data)
            design = (dest / 'sections/design.tex').read_text()
            original = before['sections/design.tex'].decode()
            self.assertEqual(design.split('\\begin{equation}')[1].split('\\end{equation}')[0], original.split('\\begin{equation}')[1].split('\\end{equation}')[0])
            paragraph = 'The worker executes each admitted request to completion before selecting the\nnext request. This non-preemptive policy avoids discarding partial execution.'
            self.assertIn(paragraph, (dest / 'sections/introduction.tex').read_text())
            self.assertIn('No latency gain appears', (dest / 'sections/evaluation.tex').read_text())

    def test_assessment_requires_actual_unchanged_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = m.prepare('local', Path(tmp) / 'task', 'none')
            assessment = {'assessor': 'unit-test fixture', 'dimensions': {
                name: {'status': 'not_observed', 'evidence': 'No behavioral model was run in this unit test.'}
                for name in m.DIMENSIONS}}
            with self.assertRaises(ValueError):
                m.assess(dest, assessment)
            (dest / 'output.md').write_text('Synthetic test output, not an agent run.')
            m.record(dest, 'unit-test only', 'test', ['file-read'])
            (dest / 'output.md').write_text('Changed output')
            with self.assertRaises(ValueError):
                m.assess(dest, assessment)
            m.record(dest, 'unit-test only', 'test', ['file-read'])
            m.assess(dest, assessment)
            self.assertEqual(json.loads((dest / 'manifest.json').read_text())['status'], 'assessed')

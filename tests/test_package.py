import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package', ROOT / 'scripts/check_package.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def tearDown(self):
        self.tmp.cleanup()

    def errors(self):
        return m.check(self.root)[0]

    def write(self, name, text):
        p = self.root / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text)

    def test_real_package(self):
        self.assertEqual(self.errors(), [])

    def test_titled_links_and_fragments(self):
        self.write('extra.md', '[Review](review-workflows.md#author-draft-review "Author route")\n[Self](#local)\n## Local\n')
        self.assertEqual(self.errors(), [])
        self.write('extra.md', '[Bad](review-workflows.md#missing "A title")')
        self.assertTrue(any('Broken anchor' in e for e in self.errors()))

    def test_required_anchor(self):
        p = self.root / 'review-workflows.md'
        p.write_text(p.read_text().replace('## Other-paper review', '## Different heading'))
        self.assertTrue(any('Missing required anchors' in e for e in self.errors()))

    def test_current_version_not_history(self):
        p = self.root / 'CHANGELOG.md'
        p.write_text(p.read_text() + '\n## 0.1.0 — historical\n')
        self.assertEqual(self.errors(), [])
        p = self.root / 'README.md'; p.write_text(p.read_text().replace('badge/skill-1.3.0-', 'badge/skill-1.0.0-'))
        self.assertTrue(any('version mismatch' in e for e in self.errors()))

    def test_language_and_privacy_are_separate(self):
        self.write('tests/behavior/inputs/local-task.md', '\u8bf7\u6da6\u8272')
        self.assertEqual(self.errors(), [])
        self.write('references/bad.md', '\u8bf7\u6da6\u8272')
        self.assertTrue(any('Non-English guide' in e for e in self.errors()))
        self.write('tests/behavior/inputs/local-task.md', '/' + 'Users/private/file')
        self.assertTrue(any('Private provenance marker' in e for e in self.errors()))

    def test_approved_patch_not_blanket_ignore(self):
        self.assertEqual(self.errors(), [])
        self.write('examples/unapproved.diff', 'temporary patch')
        self.assertTrue(any('Unexpected artifact' in e for e in self.errors()))

    def test_links_with_spaces_and_escape(self):
        self.write('space name.md', '# Target\n')
        self.write('extra.md', '[Valid](<space name.md#target> "Title")')
        self.assertEqual(self.errors(), [])
        self.write('extra.md', '[Escaped](../outside.md)')
        self.assertTrue(any('escapes package' in e for e in self.errors()))

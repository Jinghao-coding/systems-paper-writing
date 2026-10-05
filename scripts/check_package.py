#!/usr/bin/env python3
"""Check maintained Markdown links, versions, English guides and public hygiene."""
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
APPROVED_PATCHES = {'examples/author-revision.diff',
                    'validation/runs/edit-current/revision.patch'}
# Only these raw test inputs may contain non-English prose. Guides remain English.
MULTILINGUAL_INPUTS = {'tests/behavior/inputs/local-task.md'}
REQUIRED_ANCHORS = {
    'review-workflows.md': {'author-draft-review', 'other-paper-review'},
    'references/venue-guide.md': {'matching-workflow'},
    'references/systems-paper-patterns.md': {'10-research-type-review-paths'},
    'README.md': {'quick-start', 'what-it-does'},
}
LINK = re.compile(r'\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+["\'][^\n]*?["\'])?\s*\)')


def anchors(content):
    found, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+?)(?:\s+#+)?\s*$', content, re.M):
        title = re.sub(r'<[^>]*>', '', title).strip().lower()
        slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        count = counts.get(slug, 0)
        found.add(slug if count == 0 else f'{slug}-{count}')
        counts[slug] = count + 1
    found.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', content))
    return found


def check(root):
    root = Path(root).resolve()
    errors, links = [], 0
    try:
        skill = (root / 'SKILL.md').read_text()
        if not re.match(r'^---\nname: systems-paper-writing\n', skill):
            errors.append('Invalid skill identity')
        version = re.search(r'^  version: "([\d.]+)"$', skill, re.M)
        if not version:
            errors.append('Missing current version')
        else:
            current = version[1]
            readme = (root / 'README.md').read_text()
            badge = re.search(r'badge/skill-([\d.]+)-', readme)
            latest = re.search(r'^## ([\d.]+) ', (root / 'CHANGELOG.md').read_text(), re.M)
            if not badge or badge[1] != current:
                errors.append('README current version mismatch')
            if not latest or latest[1] != current:
                errors.append('Changelog current version mismatch')
            tool = (root / 'scripts/reference_tools.py').read_text()
            if f"systems-paper-writing/{current} " not in tool:
                errors.append('Reference tool current version mismatch')
        if '$systems-paper-writing' not in (root / 'agents/openai.yaml').read_text():
            errors.append('Default invocation does not match skill name')
    except (OSError, UnicodeError) as exc:
        errors.append(f'Missing or unreadable package metadata: {exc}')
    for name, required in REQUIRED_ANCHORS.items():
        path = root / name
        if not path.is_file():
            errors.append(f'Missing required guide: {name}')
        elif not required <= anchors(path.read_text()):
            errors.append(f'Missing required anchors: {name}: {sorted(required - anchors(path.read_text()))}')
    for path in root.rglob('*'):
        relative = path.relative_to(root).as_posix()
        if '.git' in path.parts or '__pycache__' in path.parts or not path.is_file():
            continue
        if path.suffix in {'.pyc', '.pdf', '.bundle', '.diff', '.patch'} and relative not in APPROVED_PATCHES:
            errors.append(f'Unexpected artifact: {relative}')
        if path.suffix not in {'.md', '.py', '.yaml', '.yml', '.txt', '.json', '.tex', '.csv', '.diff', '.patch'}:
            continue
        try:
            content = path.read_text()
        except (OSError, UnicodeError) as exc:
            errors.append(f'Unreadable text: {relative}: {exc}')
            continue
        # Checker contains these expressions; no other path gets a hygiene exemption.
        if relative != 'scripts/check_package.py' and re.search(r'/Users/|/home/|teacher-yang|NaviPerf|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----', content):
            errors.append(f'Private provenance marker: {relative}')
        if path.suffix != '.md':
            continue
        guide = relative == 'SKILL.md' or relative == 'review-workflows.md' or relative.startswith('references/')
        if guide and re.search(r'[\u4e00-\u9fff]', content):
            errors.append(f'Non-English guide: {relative}')
        if relative.startswith('tests/behavior/inputs/') and relative not in MULTILINGUAL_INPUTS and re.search(r'[\u4e00-\u9fff]', content):
            errors.append(f'Undeclared multilingual input: {relative}')
        for match in LINK.finditer(content):
            target = match[1] or match[2]
            if re.match(r'^[a-zA-Z][\w+.-]*:', target):
                continue
            filename, _, fragment = unquote(target).partition('#')
            linked = (path.parent / filename).resolve() if filename else path
            links += 1
            if not linked.is_relative_to(root):
                errors.append(f'Link escapes package: {relative}: {target}')
            elif not linked.exists():
                errors.append(f'Broken link: {relative}: {target}')
            elif fragment and linked.suffix == '.md' and fragment not in anchors(linked.read_text()):
                errors.append(f'Broken anchor: {relative}: {target}')
    return errors, links


def main():
    errors, links = check(ROOT)
    print(f'Checked {links} local Markdown links and anchors.')
    for error in errors:
        print(error)
    if not errors:
        print('Package checks passed.')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())

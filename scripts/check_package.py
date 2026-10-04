#!/usr/bin/env python3
"""Check package links, entry identity, English guides and publication hygiene."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]


def main():
    errors=[];links=0
    skill=(ROOT/'SKILL.md').read_text()
    if not re.match(r'^---\nname: systems-paper-writing\n',skill):
        errors.append('Invalid skill identity')
    if '$systems-paper-writing' not in (ROOT/'agents/openai.yaml').read_text():
        errors.append('Default invocation does not match skill name')
    for path in ROOT.rglob('*'):
        if '.git' in path.parts or '__pycache__' in path.parts or not path.is_file():continue
        relative=path.relative_to(ROOT)
        if path.suffix in {'.pyc','.diff','.pdf','.bundle'}:
            errors.append(f'Unexpected artifact: {relative}')
        if path.suffix not in {'.md','.py','.yaml','.yml','.txt'}:continue
        content=path.read_text()
        # Keep private environment paths out of public documents.
        if path.name!='check_package.py' and re.search(r'/Users/|/home/|teacher-yang|NaviPerf',content):
            errors.append(f'Private provenance marker: {relative}')
        if path.suffix=='.md':
            if path.name not in {'README.md','README.zh-CN.md'} and re.search(r'[\u4e00-\u9fff]',content):
                errors.append(f'Non-English guide: {relative}')
            for target in re.findall(r'\]\(([^)]+)\)',content):
                if '://' in target or target.startswith(('#','mailto:')):continue
                target=target.split('#')[0]
                if target:
                    links+=1
                    if not (path.parent/target).exists():errors.append(f'Broken link: {relative}: {target}')
    print(f'Checked {links} local Markdown link targets.')
    if errors:
        for error in errors:print(error)
        return 1
    print('Package checks passed.')
    return 0


if __name__=='__main__':raise SystemExit(main())

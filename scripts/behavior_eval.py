#!/usr/bin/env python3
"""Prepare blind, offline behavior tasks and capture actual outputs; no model API required."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(root):
    return {p.relative_to(root).as_posix(): digest(p) for p in sorted(root.rglob('*')) if p.is_file()}


def prepare(task, dest, variant, skill_source=None):
    tasks = json.loads((ROOT / 'tests/behavior/tasks.json').read_text())
    if task not in tasks:
        raise ValueError('Unknown task: ' + task)
    dest = Path(dest).resolve()
    if dest.exists():
        raise ValueError('Destination must not exist; preserve prior runs')
    config = tasks[task]
    dest.mkdir(parents=True)
    materials = dest / 'materials'
    materials.mkdir()
    for name in config['inputs']:
        source = ROOT / ('examples/paper' if name == 'paper' else 'tests/behavior/inputs/' + name)
        target = materials / name
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)
    if variant != 'none':
        source = Path(skill_source).resolve() if skill_source else ROOT
        skill = dest / 'skill'
        skill.mkdir()
        # Do not copy examples, tests, acceptance answers, validation or Git history.
        for name in ('SKILL.md', 'review-workflows.md', 'references', 'scripts', 'agents'):
            item = source / name
            if item.is_dir():
                shutil.copytree(item, skill / name, ignore=shutil.ignore_patterns('__pycache__'))
            elif item.is_file():
                shutil.copy2(item, skill / name)
        revision = subprocess.run(['git', '-C', str(source), 'rev-parse', 'HEAD'], capture_output=True, text=True)
        dirty = subprocess.run(['git', '-C', str(source), 'diff', '--binary', 'HEAD'], capture_output=True, text=True)
        identity = {'base_commit': revision.stdout.strip() or 'unavailable',
                    'tracked_diff_sha256': hashlib.sha256(dirty.stdout.encode()).hexdigest(),
                    'resource_sha256': snapshot(skill)}
    else:
        identity = None
    prompt = ('Use the skill in ./skill/SKILL.md. ' if variant != 'none' else '') + config['prompt']
    prompt += '\nUse only this task directory. Do not look for expected answers or other task runs. All materials are constructed public fixtures. Save the complete response as output.md.\n'
    (dest / 'TASK.md').write_text(prompt)
    manifest = {'task': task, 'variant': variant, 'status': 'prepared_not_run',
                'material_sha256': snapshot(materials), 'skill': identity,
                'task_sha256': digest(dest / 'TASK.md')}
    (dest / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return dest


def record(dest, model, host, tools):
    dest = Path(dest).resolve()
    manifest = json.loads((dest / 'manifest.json').read_text())
    if not (dest / 'output.md').is_file():
        raise ValueError('Actual full output.md is required; cannot record an unexecuted task')
    manifest.update(status='executed_unassessed', model=model, host=host,
                    available_tools=tools, output_sha256=digest(dest / 'output.md'),
                    after_material_sha256=snapshot(dest / 'materials'))
    (dest / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')


DIMENSIONS = ('issue_detection', 'false_positives', 'technical_meaning_regressions',
              'over_editing', 'scope_violations', 'actionability')


def assess(dest, assessment):
    dest = Path(dest).resolve()
    manifest = json.loads((dest / 'manifest.json').read_text())
    if manifest['status'] != 'executed_unassessed':
        raise ValueError('Record the actual execution before assessment')
    if digest(dest / 'output.md') != manifest['output_sha256']:
        raise ValueError('Output changed after recording; record the new output first')
    if not isinstance(assessment, dict) or not assessment.get('assessor'):
        raise ValueError('Identify the assessor; do not imply independent assessment')
    dimensions = assessment.get('dimensions', {})
    if set(dimensions) != set(DIMENSIONS):
        raise ValueError('Assess all six separate dimensions')
    for name, result in dimensions.items():
        if not isinstance(result, dict) or result.get('status') not in {'pass', 'partial', 'fail', 'not_observed'}:
            raise ValueError('Invalid assessment state for ' + name)
        if not isinstance(result.get('evidence'), str) or not result['evidence'].strip():
            raise ValueError('Evidence or observation limit required for ' + name)
    (dest / 'assessment.json').write_text(json.dumps(assessment, indent=2, ensure_ascii=False) + '\n')
    manifest['status'] = 'assessed'
    manifest['assessment_sha256'] = digest(dest / 'assessment.json')
    (dest / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    prep = sub.add_parser('prepare')
    prep.add_argument('--task', required=True)
    prep.add_argument('--dest', type=Path, required=True)
    prep.add_argument('--variant', choices=['none', 'previous', 'current'], default='current')
    prep.add_argument('--skill-source', type=Path)
    rec = sub.add_parser('record')
    rec.add_argument('--dest', type=Path, required=True)
    rec.add_argument('--model', required=True)
    rec.add_argument('--host', default=platform.platform())
    rec.add_argument('--tools', nargs='+', required=True)
    judge = sub.add_parser('assess')
    judge.add_argument('--dest', type=Path, required=True)
    judge.add_argument('--assessment', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'prepare':
            if args.variant == 'previous' and not args.skill_source:
                raise ValueError('previous requires --skill-source at the adopted old version')
            print(prepare(args.task, args.dest, args.variant, args.skill_source))
        elif args.command == 'record':
            record(args.dest, args.model, args.host, args.tools)
        else:
            assess(args.dest, json.loads(args.assessment.read_text()))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

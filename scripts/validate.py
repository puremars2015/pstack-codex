"""Validate package structure, local references and optional workflow configuration.

Authoring check only: requires PyYAML and jsonschema. Skills and log.py have no
third-party runtime dependencies.
"""
from pathlib import Path
import argparse
import json
import re
import sys
from urllib.parse import unquote, urlsplit
import yaml
import jsonschema


def validate(root, config=None):
    root = root.resolve()
    errors = []
    portable = json.loads((root / 'plugin.json').read_text(encoding='utf-8'))
    compat = json.loads((root / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
    if portable.get('$schema') != 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':
        errors.append('Unrecognized portable plugin schema')
    for key in ('name', 'version', 'description'):
        if portable.get(key) != compat.get(key):
            errors.append(f'Manifest mismatch: {key}')
    if not re.fullmatch(r'\d+\.\d+\.\d+', portable.get('version', '')):
        errors.append('Invalid package version')
    if compat.get('skills') != './skills/':
        errors.append('Compatibility manifest must discover ./skills/')
    if any(k in portable for k in ('skills', 'mcpServers', 'apps', 'interface')):
        errors.append('Portable manifest contains legacy-only top-level fields')
    if portable.get('extensions', {}).get('com.openai', {}).get('interface') != compat.get('interface'):
        errors.append('Manifest interface metadata differs')
    if len(compat.get('interface', {}).get('shortDescription', '')) > 30:
        errors.append('Listing shortDescription exceeds 30 characters')
    for p in root.rglob('*'):
        if p.is_symlink():
            errors.append(f'Symlink not allowed: {p.relative_to(root)}')
    seen = set()
    entries = list((root / 'skills').glob('*/SKILL.md'))
    for p in entries:
        text = p.read_text(encoding='utf-8')
        try:
            if not text.startswith('---\n'):
                raise ValueError('Missing YAML frontmatter')
            meta = yaml.safe_load(text.split('---', 2)[1])
            name = meta['name']
            if name != p.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
                raise ValueError('Skill name must match its folder')
            if name in seen or not isinstance(meta.get('description'), str) or not meta['description'].strip():
                raise ValueError('Duplicate name or missing description')
            if 'disable-model-invocation' in meta:
                raise ValueError('Unadapted invocation policy')
            seen.add(name)
        except (KeyError, ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f'{p.relative_to(root)}: {exc}')
    for p in (root / 'skills').rglob('openai.yaml'):
        policy = yaml.safe_load(p.read_text(encoding='utf-8'))
        if not isinstance(policy, dict) or ('allow_implicit_invocation' in policy.get('policy', {}) and not isinstance(policy['policy']['allow_implicit_invocation'], bool)):
            errors.append(f'Invalid invocation policy: {p.relative_to(root)}')
        if 'interface' in policy:
            ui = policy['interface']
            if not isinstance(ui, dict) or any(not isinstance(ui.get(k), str) or not ui[k].strip() for k in ('display_name', 'short_description')):
                errors.append(f'Invalid skill interface: {p.relative_to(root)}')
    for p in root.rglob('*.md'):
        text = p.read_text(encoding='utf-8')
        # Ignore fenced examples, which can contain illustrative links.
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for link in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
            link = link.strip().strip('<>')
            if urlsplit(link).scheme or link.startswith('#'):
                continue
            target = (p.parent / unquote(link.split('#', 1)[0])).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'{p.relative_to(root)}: missing/escaping link {link}')
    # The runnable workflows must not depend on removed host tools.
    forbidden = re.compile(r'\.cursor[/\\]|subagent_type|run_in_background|cloud_base_branch|grok-\d|claude-opus|/add-plugin|cursor-team-kit|bugbot', re.I)
    for p in (root / 'skills').rglob('*.md'):
        if forbidden.search(p.read_text(encoding='utf-8')):
            errors.append(f'Unsupported host reference: {p.relative_to(root)}')
    schema = json.loads((root / 'skills/poteto-mode/references/config.schema.json').read_text(encoding='utf-8'))
    jsonschema.Draft202012Validator.check_schema(schema)
    for cfg in [root / 'config.defaults.json'] + ([config] if config else []):
        try:
            jsonschema.validate(json.loads(cfg.read_text(encoding='utf-8')), schema)
        except (ValueError, jsonschema.ValidationError) as exc:
            errors.append(f'Invalid configuration {cfg}: {exc.message if hasattr(exc, "message") else exc}')
    if not entries:
        errors.append('No skill entrypoints found')
    return {'skills': len(entries), 'playbooks': len(list((root / 'skills/poteto-mode/playbooks').glob('*.md'))), 'errors': errors}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--config', type=Path)
    args = parser.parse_args()
    result = validate(args.root, args.config)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result['errors']))

"""Read-only structural checks; no network or third-party dependencies."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def audit(path, complete=False):
    root = path.resolve().parent
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    errors, warnings = [], []
    if not isinstance(data, dict):
        return {'errors': ['manifest must be an object'], 'warnings': []}

    def file(value, label):
        if not isinstance(value, str) or not value.strip():
            errors.append(f'{label}: missing path')
            return None
        p = Path(value)
        p = p if p.is_absolute() else root / p
        if not p.is_file():
            errors.append(f'{label}: file missing: {p}')
            return None
        return p

    fonts, pages = data.get('fonts', {}), data.get('pages')
    if not isinstance(fonts, dict) or not isinstance(pages, list) or not pages:
        return {'errors': ['fonts must be an object and pages a nonempty array'], 'warnings': []}
    ids, used = [], set()
    for page in pages:
        if not isinstance(page, dict):
            errors.append('page must be an object')
            continue
        pid = str(page.get('id', '')).strip()
        if not pid or pid in ids:
            errors.append(f'page {pid!r}: missing or duplicate id')
        ids.append(pid)
        file(page.get('illustration'), f'page {pid} illustration')
        if complete:
            file(page.get('preview'), f'page {pid} preview')
        mode, text = page.get('text_mode'), page.get('text', '')
        if not isinstance(text, str):
            errors.append(f'page {pid}: text must be a string')
            text = ''
        if mode not in ('none', 'separate', 'baked'):
            errors.append(f'page {pid}: unknown text_mode')
        if mode == 'none' and text.strip():
            errors.append(f'page {pid}: text on declared wordless page')
        if mode == 'baked':
            errors.append(f'page {pid}: baked text remains; uniform editable typography is incomplete')
        if mode == 'separate':
            file(page.get('text_layer'), f'page {pid} text_layer')
            if not text.strip():
                errors.append(f'page {pid}: separate text is empty')
            fid = page.get('font')
            if not isinstance(fid, str) or fid not in fonts:
                errors.append(f'page {pid}: unknown font id')
            else:
                used.add(fid)
            if page.get('kind', 'body') == 'body' and fid != data.get('body_font'):
                if page.get('font_exception_reason'):
                    warnings.append(f'page {pid}: declared font exception needs approval review')
                else:
                    errors.append(f'page {pid}: font differs from body_font without exception')
    for fid in sorted(used):
        spec = fonts[fid]
        if not isinstance(spec, dict):
            errors.append(f'font {fid}: expected object')
            continue
        p = file(spec.get('path'), f'font {fid}')
        expected = spec.get('sha256')
        if p and expected and hashlib.sha256(p.read_bytes()).hexdigest().lower() != str(expected).lower():
            errors.append(f'font {fid}: sha256 mismatch')
        if complete and not expected:
            errors.append(f'font {fid}: missing sha256 for final export')
        if complete:
            file(spec.get('license_record'), f'font {fid} license_record')
        if spec.get('usage_confirmed') is not True:
            (errors if complete else warnings).append(f'font {fid}: usage authorization not verified in record')
    exports = data.get('exports', [])
    if not isinstance(exports, list):
        errors.append('exports must be an array')
        exports = []
    for export in exports:
        if not isinstance(export, dict):
            errors.append('export must be an object')
            continue
        file(export.get('path'), 'export')
        if export.get('source_version') != data.get('version'):
            errors.append('export source_version differs from book version')
        if export.get('page_ids') != ids:
            errors.append('export page_ids differs from complete page order')
        if complete and export.get('visually_verified') is not True:
            errors.append('export lacks recorded visual verification')
    if complete and not exports:
        errors.append('no final export recorded')
    warnings.append('Structural checks only; inspect actual letters, art continuity, licenses and rendered exports separately.')
    return {'page_count': len(pages), 'errors': errors, 'warnings': warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--complete', action='store_true')
    args = parser.parse_args()
    try:
        result = audit(args.manifest, args.complete)
    except (OSError, ValueError, TypeError) as exc:
        result = {'errors': [str(exc)], 'warnings': []}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['errors'] else 0


if __name__ == '__main__':
    sys.exit(main())

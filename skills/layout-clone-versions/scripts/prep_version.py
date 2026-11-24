"""Build one layout version of a fixture site and package it as a deploy zip.

Usage (--site, --name and --canonical-to are required so another site never inherits HireMilo's values):
  python3 -I prep_version.py --label v9 --worktree ~/projects/static-sites-milo-v9 \
      --site site-8 --out-root <scratch dir> --bridge-dir <scratch dir>/bridge \
      --name hiremilo --canonical-to https://hiremilo.co.uk [--skin milo] [--canonical-from https://site-8.example.test]

Steps: harness build (SKIN=<skin>) -> flat folder, each page placed by the `path` of its own fixture
-> noindex _headers and robots.txt -> canonical host rewrite -> link audit -> <bridge-dir>/<name>-<label>.zip
(zip root = site root). Prints the audit result. Exit code 1 when the build fails or a link is unresolved.
Fixture hosts stay on example.test in the repo (the fixture guard allows only that); the rewrite happens here, in the built pages only.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('--label', required=True)
ap.add_argument('--worktree', required=True)
ap.add_argument('--site', required=True)
ap.add_argument('--skin', default='milo')
ap.add_argument('--out-root', required=True)
ap.add_argument('--bridge-dir', required=True)
ap.add_argument('--name', required=True)
ap.add_argument('--canonical-from', default=None)
ap.add_argument('--canonical-to', required=True)
a = ap.parse_args()

repo = Path(a.worktree).expanduser()
harness = repo / 'harness'
src = harness / 'dist'
fix = harness / 'fixtures' / a.site
out = Path(a.out_root).expanduser() / f'{a.name}-{a.label}'
bridge = Path(a.bridge_dir).expanduser()
host_from = a.canonical_from or f'https://{a.site}.example.test'

if out.exists():
    shutil.rmtree(out)  # scratch folder of an earlier run of this script
shutil.rmtree(src, ignore_errors=True)
r = subprocess.run(['npx', 'astro', 'build'], cwd=harness, env=dict(os.environ, SKIN=a.skin), capture_output=True, text=True, timeout=280)
print('build rc', r.returncode)
if r.returncode:
    print(r.stderr[-600:])
    sys.exit(1)

out.mkdir(parents=True)
for d in ('_astro', 'hmstatic'):
    if (src / d).exists():
        shutil.copytree(src / d, out / d)
if (src / 'assets').exists():
    shutil.copytree(src / 'assets', out / 'assets')

canon = re.compile(r'(<link rel="canonical" href=")' + re.escape(host_from) + r'([^"]*")')
placed = 0
for f in sorted(fix.glob('*.json')):
    doc = json.loads(f.read_text())
    html = (src / a.site / f.stem / 'index.html').read_text()
    html = canon.sub(lambda m: m.group(1) + a.canonical_to + m.group(2), html)
    if doc['view'] == 'NotFound':
        (out / '404.html').write_text(html)  # the fixture path is not a real URL
    else:
        path = doc['path']
        t = out / 'index.html' if path == '/' else out / path.strip('/') / 'index.html'
        t.parent.mkdir(parents=True, exist_ok=True)
        t.write_text(html)
    placed += 1
(out / '_headers').write_text('/*\n  X-Robots-Tag: noindex, nofollow\n')
(out / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')

bad = []
for page in out.rglob('*.html'):
    h = page.read_text()
    urls = re.findall(r'(?:href|src)="(/[^"#?]*)', h)
    for ss in re.findall(r'srcset="([^"]*)"', h):
        urls += [u.split()[0] for u in ss.split(',') if u.strip().startswith('/')]
    for u in urls:
        p = out / u.lstrip('/')
        if u != '/' and not (p.is_file() or (p / 'index.html').is_file()):
            bad.append(f'{page.relative_to(out)} -> {u}')
print('placed', placed, 'pages | unresolved links', len(bad), bad[:5])

bridge.mkdir(parents=True, exist_ok=True)
zp = bridge / f'{a.name}-{a.label}.zip'
with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in sorted(out.rglob('*')):
        if f.is_file():
            z.write(f, f.relative_to(out).as_posix())
home = (out / 'index.html').read_text()
print(zp, zp.stat().st_size, 'bytes | canonical:', re.findall(r'rel="canonical" href="([^"]*)"', home)[:1])
sys.exit(1 if bad else 0)

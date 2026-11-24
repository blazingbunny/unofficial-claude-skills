#!/usr/bin/env python3
"""SEO inventory and SEO diff of rendered HTML (what crawlers see). Read-only, stdlib only.

  seoscan.py scan <page.html | folder> [--json]
        Inventory of every SEO signal in one page, or in every .html under a folder (for example the built
        site/ folder). Each heading, link, image and id is tagged with the page part that holds it: the nearest
        ancestor with a data-part attribute, an id, or a semantic region (header, nav, main, section, footer...).
        --json prints the full inventory (a folder gives one entry per file).
  seoscan.py diff <before> <after> [--host=old.host=new.host]
        Every SEO difference between two pages, or between two folders (files are matched by relative path).
        Exit code 1 if any difference. --host rewrites a host first (for example a preview host to the live host).
  Page parts are shown as  data-part=hero  or  #contact  or  section.services  or  header  or  footer.

Signals (what each one is and why it matters):
  head:      title, meta description, robots, canonical, hreflang, Open Graph / Twitter, JSON-LD @types and
             FAQ question count, <html lang>
  content:   heading outline (tag, text, order, page part); visible word count
  links:     href, rel, target, title, anchor text, page part; internal vs external; <button> pretending to be a
             link; #anchor links and whether their id target exists
  images:    file, alt, width/height, loading, inside <figure>/<figcaption>, page part
  structure: element ids, semantic tags (header nav main article section aside footer), lists, tables, iframes
Build the site first (the built HTML is what crawlers see), then scan the built folder.
"""
import json, re, sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

SEMANTIC = {'header', 'nav', 'main', 'article', 'section', 'aside', 'footer'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
SKIP_TEXT = {'script', 'style', 'noscript', 'template', 'svg'}
HEADING = re.compile(r'h[1-6]')


def part_of(tag, a):
    """Name of the page part this element is, or None. data-part wins, then id, then a semantic region."""
    if a.get('data-part'):
        return f"data-part={a['data-part']}"
    if a.get('id'):
        return f"#{a['id']}"
    if tag in SEMANTIC:
        cls = a.get('class', '').split()
        return f"{tag}.{cls[0]}" if cls else tag
    return None


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []            # (tag, attrs dict, part name or None)
        self.head = {'title': '', 'meta': {}, 'canonical': '', 'hreflang': [], 'jsonld': [], 'lang': ''}
        self.headings, self.links, self.images, self.ids = [], [], [], []
        self.semantic, self.counts = Counter(), Counter()
        self.microdata = []
        self.words = 0
        self._text_target = None   # list collecting text for the open heading / title
        self._jsonld = None

    def part(self):
        for _, _, own in reversed(self.stack):
            if own:
                return own
        return '-'

    def handle_starttag(self, tag, attrs):
        a = {k: (v or '') for k, v in attrs}
        if tag not in VOID:
            self.stack.append((tag, a, part_of(tag, a)))
        if a.get('id'):
            self.ids.append((a['id'], self.part()))
        if tag == 'html':
            self.head['lang'] = a.get('lang', '')
        elif tag == 'meta':
            k = a.get('name') or a.get('property')
            if k and (k in ('description', 'robots') or k.startswith(('og:', 'twitter:'))):
                self.head['meta'][k] = a.get('content', '')
        elif tag == 'link':
            rel = a.get('rel', '').lower()
            if rel == 'canonical':
                self.head['canonical'] = a.get('href', '')
            elif rel == 'alternate' and a.get('hreflang'):
                self.head['hreflang'].append((a['hreflang'], a.get('href', '')))
        elif tag == 'script' and 'ld+json' in a.get('type', ''):
            self._jsonld = []
        elif tag == 'title' and not self.head['title']:
            self._text_target = ['title', []]
        elif HEADING.fullmatch(tag):
            self._text_target = ['h', [], tag, self.part()]
        elif tag == 'a':
            self.links.append({'href': a.get('href'), 'rel': a.get('rel', ''), 'target': a.get('target', ''),
                               'title': a.get('title', ''), 'part': self.part(), 'text': [],
                               'in_heading': any(HEADING.fullmatch(t) for t, _, _ in self.stack[:-1])})
        elif tag == 'button' and (a.get('data-action-link') or a.get('onclick')):
            self.links.append({'href': None, 'rel': '', 'target': '', 'title': '', 'part': self.part(),
                               'text': [], 'in_heading': False, 'button': True})
        elif tag == 'img':
            in_fig = any(t == 'figure' for t, _, _ in self.stack)
            self.images.append({'src': a.get('src', '').split('?')[0].rsplit('/', 1)[-1], 'alt': a.get('alt'),
                                'wh': bool(a.get('width') and a.get('height')),
                                'loading': a.get('loading', ''), 'figure': in_fig, 'part': self.part()})
        if 'itemprop' in a or 'itemscope' in a:
            self.microdata.append((self.part(), f"{tag} {a.get('itemprop') or a.get('itemtype', '')}"[:60]))
        if tag in SEMANTIC:
            self.semantic[tag] += 1
        if tag in ('ul', 'ol', 'table', 'iframe', 'figcaption', 'details'):
            self.counts[tag] += 1

    def handle_endtag(self, tag):
        if tag == 'script' and self._jsonld is not None:
            self.head['jsonld'].append(''.join(self._jsonld)); self._jsonld = None
        if self._text_target:
            t = self._text_target
            if t[0] == 'title' and tag == 'title':
                self.head['title'] = ' '.join(''.join(t[1]).split()); self._text_target = None
            elif t[0] == 'h' and tag == t[2]:
                self.headings.append((t[2], ' '.join(''.join(t[1]).split())[:90], t[3])); self._text_target = None
        if tag not in VOID:
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break

    def handle_data(self, data):
        if self._jsonld is not None:
            self._jsonld.append(data); return
        if any(t in SKIP_TEXT for t, _, _ in self.stack):
            return
        if self._text_target:
            self._text_target[1].append(data)
        open_links = [l for l in self.links[-3:] if any(t == 'a' for t, _, _ in self.stack)]
        if open_links:
            open_links[-1]['text'].append(data)
        if any(t == 'body' for t, _, _ in self.stack):
            self.words += len(data.split())


def ld_types(blocks):
    types, faq_q = Counter(), 0
    def walk(o):
        nonlocal faq_q
        if isinstance(o, dict):
            t = o.get('@type')
            for x in (t if isinstance(t, list) else [t]):
                if x: types[x] += 1
            if t == 'FAQPage':
                faq_q += len(o.get('mainEntity', []) or [])
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    for b in blocks:
        try: walk(json.loads(b))
        except Exception: types['(invalid JSON-LD)'] += 1
    return dict(types), faq_q


HOSTMAP = []   # (from, to) host rewrites for diff, e.g. preview host -> live host (--host a=b)


def normalise(html):
    for a, b in HOSTMAP:
        html = html.replace(a, b)
    # Cloudflare email obfuscation differs on every request: compare the presence, not the token
    return re.sub(r'/cdn-cgi/l/email-protection#[0-9a-f]+', '/cdn-cgi/l/email-protection#EMAIL', html)


def inventory(path):
    s = Scan(); s.feed(normalise(Path(path).read_text(encoding='utf-8', errors='replace')))
    host = urlparse(s.head['canonical']).netloc
    links = []
    for l in s.links:
        href = l['href']
        kind = 'button-no-href' if l.get('button') else ('anchor' if href and href.startswith('#') else
               ('internal' if href and (href.startswith('/') or urlparse(href).netloc in ('', host)) else 'external'))
        links.append({**l, 'kind': kind, 'text': ' '.join(''.join(l['text']).split())[:60]})
    ids = {i for i, _ in s.ids}
    types, faq_q = ld_types(s.head['jsonld'])
    return {
        'head': {'title': s.head['title'], 'lang': s.head['lang'], 'canonical': s.head['canonical'],
                 'meta': s.head['meta'], 'hreflang': s.head['hreflang'], 'jsonld_types': types, 'faq_questions': faq_q},
        'headings': s.headings, 'links': links, 'images': s.images, 'ids': s.ids,
        'broken_anchors': sorted({l['href'] for l in links if l['kind'] == 'anchor' and len(l['href']) > 1 and l['href'][1:] not in ids}),
        'semantic': dict(s.semantic), 'counts': dict(s.counts), 'words': s.words,
        'microdata': s.microdata,
    }


def by_part(items, top=4):
    c = Counter(x['part'] for x in items).most_common(top)
    return ', '.join('%s %d' % (p, n) for p, n in c) or '-'


def summary(inv):
    h, L, I = inv['head'], inv['links'], inv['images']
    print(f"title: {h['title'][:80]}\ncanonical: {h['canonical']}  robots: {h['meta'].get('robots', '-')}  lang: {h['lang']}")
    print(f"meta description: {'yes' if h['meta'].get('description') else 'MISSING'}; OG tags {sum(k.startswith('og:') for k in h['meta'])}; "
          f"JSON-LD {h['jsonld_types']}; FAQ questions {h['faq_questions']}")
    print(f"headings {len(inv['headings'])}: " +
          ', '.join(f"{t}x{n}" for t, n in sorted(Counter(t for t, _, _ in inv['headings']).items())))
    for tag, text, part in inv['headings']:
        print(f"   {tag} [{part}] {text[:60]}")
    k = Counter(l['kind'] for l in L)
    print(f"links {len(L)}: {dict(k)}; nofollow {sum('nofollow' in l['rel'] for l in L)}; "
          f"sponsored/ugc {sum(('sponsored' in l['rel']) or ('ugc' in l['rel']) for l in L)}; title attr {sum(bool(l['title']) for l in L)}; "
          f"links inside headings {sum(l['in_heading'] for l in L)}")
    print(f"   links by part: {by_part(L)}")
    print(f"images {len(I)}: alt missing {sum(i['alt'] is None for i in I)}, alt empty "
          f"{sum(i['alt'] == '' for i in I)}, in <figure> {sum(i['figure'] for i in I)}, no width/height {sum(not i['wh'] for i in I)}")
    print(f"   images by part: {by_part(I)}")
    no_alt = ['%s [%s]' % (i['src'], i['part']) for i in I if i['alt'] is None][:5]
    if no_alt:
        print('   images with no alt: ' + ', '.join(no_alt))
    print(f"ids {len(inv['ids'])}; broken #anchors {inv['broken_anchors'] or 'none'}; semantic {inv['semantic']}; "
          f"{inv['counts']}; words {inv['words']}")


def keyset(inv):
    """Comparable SEO facts. The page part is left out so a moved element is not a difference."""
    h = inv['head']
    out = Counter()
    for k in ('title', 'canonical', 'lang'):
        out[f'head {k}: {h[k]}'] += 1
    for k, v in h['meta'].items():
        if k not in ('og:updated_time', 'article:modified_time'):   # changes on every save
            out[f'meta {k}: {v[:120]}'] += 1
    for t, n in h['jsonld_types'].items():
        out[f'JSON-LD @type {t}'] += n
    out[f'FAQ questions: {h["faq_questions"]}'] += 1
    for tag, text, _ in inv['headings']:
        out[f'heading {tag}: {text}'] += 1
    for l in inv['links']:
        out[f"link {l['kind']} href={l['href']} rel={' '.join(sorted(l['rel'].split()))} target={l['target']} title={l['title']}"] += 1
    for i in inv['images']:
        out[f"image {i['src']} alt={i['alt']} figure={i['figure']}"] += 1
    for i, _ in inv['ids']:
        if not i.startswith('astro-'):
            out[f'id {i}'] += 1
    for k, v in {**inv['semantic'], **inv['counts']}.items():
        out[f'tag <{k}> count {v}'] += 1
    out[f'broken anchors {inv["broken_anchors"]}'] += 1
    for _, what in inv['microdata']:
        out[f'microdata {what}'] += 1
    return out


def html_files(path):
    """{relative name: Path} for a file, or for every .html under a folder."""
    p = Path(path)
    if p.is_dir():
        return {str(f.relative_to(p)): f for f in sorted(p.rglob('*.html'))}
    return {p.name: p}


def diff_pair(pa, pb, label=''):
    ia, ib = inventory(pa), inventory(pb)
    a, b = keyset(ia), keyset(ib)
    gone, new = a - b, b - a
    order = [t for t, _, _ in ia['headings']] != [t for t, _, _ in ib['headings']]
    pre = f'{label}: ' if label else ''
    for k, n in sorted(gone.items()): print(f'- {pre}{k}' + (f'  (x{n})' if n > 1 else ''))
    for k, n in sorted(new.items()): print(f'+ {pre}{k}' + (f'  (x{n})' if n > 1 else ''))
    if order and not gone and not new:
        print(f'~ {pre}heading order changed')
    return sum(gone.values()) + sum(new.values()) + (1 if order and not gone and not new else 0)


def main():
    for a in [x for x in sys.argv if x.startswith('--host=')]:
        HOSTMAP.append(tuple(a[7:].split('=', 1)))
        sys.argv.remove(a)
    if len(sys.argv) >= 3 and sys.argv[1] == 'scan':
        files = html_files(sys.argv[2])
        if not files:
            print(f'no .html files found in {sys.argv[2]}'); sys.exit(2)
        is_dir = Path(sys.argv[2]).is_dir()
        if '--json' in sys.argv:
            invs = {name: inventory(f) for name, f in files.items()}
            print(json.dumps(invs if is_dir else next(iter(invs.values())), indent=1, default=list))
        else:
            for name, f in files.items():
                if is_dir:
                    print(f'== {name}')
                summary(inventory(f))
    elif len(sys.argv) == 4 and sys.argv[1] == 'diff':
        fa, fb = html_files(sys.argv[2]), html_files(sys.argv[3])
        total = 0
        if Path(sys.argv[2]).is_file() and Path(sys.argv[3]).is_file():
            total = diff_pair(sys.argv[2], sys.argv[3])
        else:
            for name in sorted(set(fa) | set(fb)):
                if name not in fa:
                    print(f'+ page only in after: {name}'); total += 1
                elif name not in fb:
                    print(f'- page only in before: {name}'); total += 1
                else:
                    total += diff_pair(fa[name], fb[name], name)
        print(f'SEO differences: {total}')
        sys.exit(1 if total else 0)
    else:
        print(__doc__); sys.exit(2)


if __name__ == '__main__':
    main()

"""Check built output for broken local URLs and accidentally published examples."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.h1 = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
errors = []
parsed = {}
for file in root.rglob('*.html'):
    content = file.read_text()
    page = Page()
    page.feed(content)
    parsed[file] = page
    for marker in ('GitHub University', 'Paper Title Number', 'Professor Hub', 'Put the PDF report at', 'May–Aug 2026'):
        if marker in content:
            errors.append(f'{file.relative_to(root)}: stale/template content: {marker}')
    if 'http-equiv="refresh"' not in content and file.name != 'redirect.html' and page.h1 != 1:
        errors.append(f'{file.relative_to(root)}: expected one H1, found {page.h1}')

for file, page in parsed.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme and url.scheme not in ('http', 'https'):
            continue
        if url.netloc and url.netloc != 'kvnfltr.github.io':
            continue
        path = unquote(url.path)
        target = root / path.lstrip('/') if path.startswith('/') else file.parent / path if path else file
        target = target.resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{file.relative_to(root)}: missing {link}')
        elif url.fragment and target in parsed and unquote(url.fragment) not in parsed[target].ids:
            errors.append(f'{file.relative_to(root)}: missing anchor {link}')

for required in ('index.html', 'portfolio/index.html', 'cv/index.html', 'sitemap.xml', '404.html'):
    if not (root / required).exists():
        errors.append(f'Missing required output: {required}')
for forbidden in ('publications', 'talks', 'teaching', 'markdown', 'year-archive', 'terms'):
    if (root / forbidden).exists():
        errors.append(f'Unexpected template route: {forbidden}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(parsed)} HTML pages, local assets and anchors; no template content.')

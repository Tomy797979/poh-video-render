#!/usr/bin/env python3
import json, os, re

items = []
for i in range(1, 6):
    line = os.environ.get(f'PRODUCT_{i}', '').strip()
    if not line:
        continue
    if '|' in line:
        url, name = line.split('|', 1)
        url  = url.strip()
        name = re.sub(r'[^a-z0-9-]', '-', name.strip().lower()).strip('-')
    else:
        url  = line.strip()
        asin = re.search(r'[A-Z0-9]{10}', url)
        name = asin.group(0).lower() if asin else f'product-{i}'
    if url:
        items.append({'url': url, 'name': name})

matrix = {'include': items}
with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    f.write(f'matrix={json.dumps(matrix)}\n')
    f.write(f'count={len(items)}\n')

print(f'Parsed {len(items)} product(s):')
for item in items:
    print(f'  [{item["name"]}]  {item["url"]}')

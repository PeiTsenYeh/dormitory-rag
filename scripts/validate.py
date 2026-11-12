"""Run with Python standard library: python3 scripts/validate.py."""
import json,re
from pathlib import Path
from html.parser import HTMLParser
root=Path(__file__).resolve().parents[1]
s=(root/'content/guides.js').read_text()
assert s.startswith('window.DORM_GUIDES = ')
data=json.loads(s.removeprefix('window.DORM_GUIDES = ').strip().removesuffix(';'))
assert data
slugs=[]
for g in data:
 for k in ['slug','category','title','intro','sourceVersion','updated','sections']:assert g.get(k),(g.get('slug'),k)
 assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',g['slug'])
 assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',g['updated'])
 for sec in g['sections']:
  for k in ['heading','body','reference']:assert isinstance(sec.get(k),str) and sec[k].strip()
 slugs.append(g['slug'])
assert len(slugs)==len(set(slugs))
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('src','href') and v and not v.startswith(('#','https://','http://','mailto:')):
    assert not v.startswith('/'),v
    assert (root/v).is_file(),v
parser=Links();parser.feed((root/'index.html').read_text())
for path in (root/'notebooks').glob('*.ipynb'):
 nb=json.loads(path.read_text())
 assert nb['nbformat']==4
 for c in nb['cells']:
  if c['cell_type']=='code': assert not c.get('outputs')
assert (root/'AGENTS.md').is_file()
print(f'PASS: {len(data)}指南、{len(slugs)}唯一slug、來源欄位、相對檔案連結、Notebook結構與清除輸出。')

import re
import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
text = text.replace("''", '').split('\n')

memo, flag = [], False
template = '基礎情報'
p = re.compile('\|(.+?)=(.+)')
p1 = re.compile('\{\{' + template)
p2 = re.compile('\}\}')
p3 = re.compile('\|')
p4 = re.compile('<ref(\s|>).+?(</ref>|$)')

for t in text:
    if flag:
        if p2.match(t):
            break
        if p3.match(t):
            memo.append(p4.sub('', t.strip()))
    if p1.match(t):
        flag = True

check = {}
ans = {}
for tmp in [p.match(m) for m in memo]:
    check[tmp.group(1).replace(' ', '')] = tmp.group(2).replace(' ', '')

check1 = re.compile("'+")
check2 = re.compile('\[\[(.+\||)(.+?)\]\]')
check3 = re.compile('\{\{(.+\||)(.+?)\}\}')
check4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')

for k, v in check.items():
    v = check1.sub('', v)
    v = check2.sub(r'\2', v)
    v = check3.sub(r'\2', v)
    v = check4.sub('', v)
    ans[k] = v
print(ans)

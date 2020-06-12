import re
import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
text = text.replace("''", '').split('\n')

memo, flag = [], False
template = '基礎情報'
check = re.compile('\|(.+?)\s=\s(.+)')
check1 = re.compile('\{\{' + template)
check2 = re.compile('\}\}')
check3 = re.compile('\|')
check4 = re.compile('<ref(\s|>).+?(</ref>|$)')

for t in text:
    if flag:
        if check2.match(t):
            break
        if check3.match(t):
            memo.append(check4.sub('', t.strip()))
    if check1.match(t):
        flag = True

ans = {}
for tmp in [check.match(m) for m in memo]:
    if tmp:
        ans[tmp.group(1)] = tmp.group(2)

r1 = re.compile("'+")
r2 = re.compile('\[\[(.+\||)(.+?)\]\]')
r3 = re.compile('\{\{(.+\||)(.+?)\}\}')
r4 = re.compile('<\s*?/*?\s*?br\s*?/*?\s*>')

for k, v in ans.items():
    v = r1.sub('', v)
    v = r2.sub(r'\2', v)
    v = r3.sub(r'\2', v)
    v = r4.sub('', v)
    ans[k] = v
print(ans)

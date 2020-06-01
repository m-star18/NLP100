import re
import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0].split('\n')

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

ans = {}
for tmp in [p.match(m) for m in memo]:
    ans[tmp.group(1).replace(' ', '')] = tmp.group(2).replace(' ', '')
print(ans)

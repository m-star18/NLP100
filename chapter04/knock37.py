from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib


def parse_line(check):
    res = []
    for li in check.split('\n'):
        if li == '':
            return res
        (surface, rest) = li.split('\t')
        rest = rest.split(',')
        parse_dict = {'surface': surface, 'base': rest[6], 'pos': rest[0], 'pos1': rest[1]}
        res.append(parse_dict['base'])


memo = []
ans = []
with open('neko.txt.mecab', mode='rt', encoding='utf-8') as f:
    for line in f.read().split('EOS\n'):
        if line != '':
            memo.append(line)

for line in memo:
    check = parse_line(line)
    if '猫' in check:
        check.remove('猫')
        ans += check
ans = Counter(ans).most_common()[:10]

x = []
y = []
for word, cnt in ans:
    x.append(word)
    y.append(cnt)
plt.figure(figsize=(8, 8))
plt.barh(x, y)
plt.show()

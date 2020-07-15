import math
from collections import Counter
import matplotlib.pyplot as plt


def parse_line(check):
    res = []
    for li in check.split('\n'):
        if li == '':
            return res
        (surface, rest) = li.split('\t')
        rest = rest.split(',')
        parse_dict = {'surface': surface, 'base': rest[6], 'pos': rest[0], 'pos1': rest[1]}
        res.append(made_words(parse_dict))


def made_words(check):
    return check['base'] + '-' + check['pos'] + '-' + check['pos1']


memo = []
ans = []
with open('neko.txt.mecab', mode='rt', encoding='utf-8') as f:
    for line in f.read().split('EOS\n'):
        if line != '':
            memo.append(line)

for line in memo:
    ans += parse_line(line)
ans = Counter(ans).most_common()

x = [math.log(i + 1) for i in range(len(ans))]
y = [math.log(v[1]) for v in ans]
plt.figure(figsize=(8, 8))
plt.scatter(x, y)
plt.show()

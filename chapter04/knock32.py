def parse_line(check):
    res = []
    for li in check.split('\n'):
        if li == '':
            return res
        (surface, rest) = li.split('\t')
        rest = rest.split(',')
        parse_dict = {'surface': surface, 'base': rest[6], 'pos': rest[0], 'pos1': rest[1]}
        res.append(parse_dict)


memo = []
ans = []
with open('neko.txt.mecab', mode='rt', encoding='utf-8') as f:
    for line in f.read().split('EOS\n'):
        if line != '':
            memo.append(line)

for line in memo:
    for block in parse_line(line):
        if block['pos'] == '動詞':
            ans.append(block['base'])
print(ans)

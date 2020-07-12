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
    line = parse_line(line)
    for bf, block, af in zip(line, line[1:], line[2:]):
        if bf['pos'] == af['pos'] == '名詞' and block['base'] == 'の':
            ans.append(bf['surface'] + block['surface'] + af['surface'])
print(ans)

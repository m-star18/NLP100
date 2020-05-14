def n_gram(text, n):
    return [text[index: index + n] for index in range(len(text) + 1 - n)]


text1 = 'paraparaparadise'
text2 = 'paragraph'
x = set(n_gram(text1, 2))
y = set(n_gram(text2, 2))

print('和集合: {}'.format(x | y))
print('積集合: {}'.format(x & y))
print('差集合: {}'.format(x - y))
print('se' in (x & y))

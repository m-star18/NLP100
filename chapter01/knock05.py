def n_gram(text, n):
    return [text[index: index + n] for index in range(len(text) + 1 - n)]


text = 'I am an NLPer'
for i in range(1, 4):
    print(n_gram(text, i))
    print(n_gram(text.split(' '), i))

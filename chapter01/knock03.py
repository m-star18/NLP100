text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
text.replace(',', '').replace('.', '')
answer = [len(t) for t in text.split()]
print(answer)

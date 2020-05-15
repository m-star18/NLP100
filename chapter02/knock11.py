text = [data.strip().replace('\t', ' ') for data in open('popular-names.txt')]
print('\n'.join(text))

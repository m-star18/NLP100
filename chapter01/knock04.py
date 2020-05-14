from collections import defaultdict

text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
text.replace('.', '').replace(',', '')
dict = defaultdict(int)
for i, t in enumerate(text.split()):
    dict[t[:(i % 2) + 1]] = i + 1
print(dict)

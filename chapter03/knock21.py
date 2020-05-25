import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
ans = list(filter(lambda x: 'Category' in x, text.split('\n')))
print(ans)

import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
print(df.query('title=="イギリス"')['text'].values[0])

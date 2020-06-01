import re
import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', text):
    print(file[1])

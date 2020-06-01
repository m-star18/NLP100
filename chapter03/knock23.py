import re
import pandas as pd

df = pd.read_json('jawiki-country.json', lines=True)
text = df.query('title=="イギリス"')['text'].values[0]
for section in re.findall(r'(=+)([^=]+)\1\n', text):
    print('{}: {}'.format(section[0], len(section[0]) - 1))

import sys
import pandas as pd

if len(sys.argv) == 1:
    print('Set arg n!!')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    print(df.head(n))

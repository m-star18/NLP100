import sys
import pandas as pd

if len(sys.argv) == 1:
    print('Set arg n!!')
else:
    n = int(sys.argv[1])
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    n_split = -(-len(df) // n)
    for i in range(n):
        df.loc[i * n_split:(i + 1) * n_split].to_csv(f'knock16/{i}', sep='\t', index=False, header=None)

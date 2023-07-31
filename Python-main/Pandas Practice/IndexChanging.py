import pandas as pd

saurabh = pd.read_csv('saurabh.csv')

print(saurabh)

saurabh.index = ['first', 'second', 'third', 'fourth']
print()
print('index no. is changing ')
print(saurabh)

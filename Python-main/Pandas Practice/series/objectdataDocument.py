import pandas as pd

dic = {"name": ['javascript', 'python', 'GoLang'],
       "por": [11, 22, 33, 44],
       "ranking": [1, 2, 3, 4]
       }
d = pd.Series(dic)
print(d)
print(pd.Series(11))
print(type(d))

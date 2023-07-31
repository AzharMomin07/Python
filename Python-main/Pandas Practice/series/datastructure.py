import pandas as pd

x = [1, 2, 3, 4]
data = pd.Series(x, index=['first', 'second', 'third', 'fourth'], dtype="float", name="Python")
print(x)
print(type(data))
print(data[2])

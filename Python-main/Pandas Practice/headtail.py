import numpy as np
import pandas as pd

dict1 = {
    "Name": ['saurabh', 'shankar', 'ajit', 'akash'],
    "Marks": [90, 89, 87, 86],
    "City": ['Sangamner', 'Kokanewadi', 'mumbai', 'naviMumbai']
}
df = pd.DataFrame(dict1)
print(df)
print()
print("first two data:", df.head(2))  # first two rows print
print("last two data:", df.tail(2))   # last two rows print


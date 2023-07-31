import numpy as np
import pandas as pd

dict1 = {
    "Name": ['saurabh', 'shankar', 'ajit', 'akash'],
    "Marks": [90, 89, 87, 86],
    "City": ['Sangamner', 'Kokanewadi', 'mumbai', 'naviMumbai']
}
pf = pd.DataFrame(dict1)  # Generate Dframe - table
print(pf.to_csv('file.csv'))  # Generate csv file
print(pf.to_csv('files.csv', index=False))  # using index = false we are not get index position


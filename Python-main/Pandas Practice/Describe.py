import pandas as pd

dict1 = {
    "name": ['saurabh', 'shankar', 'Shailesh', "akash"],
    "marks": [90, 89, 88, 87],
    "number": [1, 2, 3, 4],
    "City": ["sangamner", "kokanewadi", "shirdi", "Nashik"]
}
dd = pd.DataFrame(dict1)
print(dd)
print()
print(dd.describe())

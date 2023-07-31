import pandas as pd

saurabh = pd.read_csv('saurabh.csv')  # read pdf

print(saurabh)
print()
print("specific data we want to print")
# when we want to change any specific value

print(saurabh['Speed'][0])  # update karna baki

saurabh.to_csv('saurabh1.csv')  # Convert to csv

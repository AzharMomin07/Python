# import pandas as pd
#
# # replace "data.xlsx" with the name and path of your Excel file
# data = pd.read_excel("C:/Users/CA-SHUBHAMKANDEKAR/Downloads/ADM - All Providers Report DMF 4.3.23 2 of 2.xlsx")
#
# # display the first 5 rows of the data
# print(data.head(13))


import pandas as pd

# Set display options to show all columns
pd.set_option('display.max_columns', None)

# Replace "data.xlsx" with the name and path of your Excel file
data = pd.read_excel("C:/Users/CA-SHUBHAMKANDEKAR/Downloads/ADM - All Providers Report DMF 4.3.23 2 of 2.xlsx")

# Display all the rows and columns of the data
print(data)

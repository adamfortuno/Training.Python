#!/usr/bin/env python3

# import pandas as pd

# workbook = pd.ExcelFile("sales.xlsx")

# ## Print out the sheet names in the workbook
# print("Printing the names of the sheets in the workbook")
# print(workbook.sheet_names)

# ## Create an object for the `Sales` worksheet
# sales = workbook.parse("sales")

# ## Display all data in a column
# print("Printing all sales data")
# print(sales.Date)

# ## Print the sum of all sales
# print(f"The sales total is ${sales.Amount.sum()}")

# ## Print a single row
# print(sales.loc[0])

# ## Print a specific field from a row
# print(sales.loc[0].Amount)

# ## Search for rows by customer name
# ## Step-1: Creating an index on customer first
# sales.set_index("Customer", inplace=True)
# ## Step-2: Searching for sales by customer
# print(sales.loc["MMC Inc."])

# sales = sales.reset_index()
# sales["Invoice"]


# sales.loc[ sales["Amount"] > 1800 ]


# Pandas delivers data in the form of dataframes and series:

# * A series can only contain a single list with index.
# * A dataframe is composed of multiple series, a collection of series.

# ## Returns a series
# sales["Amount"] > 1800

def foo(name):
    whatevs = 'something'

    def bar(name):
        return ' '.join([name, whatevs])

    return bar


something = foo('kenny')
print(something('adam'))
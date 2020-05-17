# Python Modules

## Extensibility - Modules and Packages

You can locate the name of a module in it's "__name__" attribute

The docstring of a module/function can be found in it's "__doc__" attribute

The following commands imports a module:

```python
## Option-1: Import a Module
import <file_name_without_file_extension>

import math
math.factorial(10)

## Option-2: Import Specific Function
from <module> import <function>, <function>

from math import factorial, assign
factorial(10)

## Option-3: Import Specific Function Under a Different Name
from <module> import <function> as <alias>
```

The following commands import functions and objects from a script:

```python
## Import all code from a file
from <file_name_without_file_extension> import *


## Imports single class from specified file
from <file_name_without_file_extension> import <class_name>
t = <ClassName>()
```

You can list the modules on your system with `help('modules')`.

# Modules: OS

The OS module controls things on the host. For example, you can use the OS module to execute shell commands care-of the `system()` method:

```Python
import os

## On windows...
os.system('CLS')

## On MacOS
os.system('clear')
```

## Modules: Time

The time module gives you all sorts of objects and methods to work with dates and times.

```python
import time as time

## Save the local time; print hour and minute
now = time.localtime()
now.tm_hour
now.tm_min

## Time since the epoch
time.time()

## Puts your routine to sleep for the specified number
## of seconds
time.sleep(<seconds>)
```

## Modules: Matplotlib

Matplotlib is an external module used to make charts and graphs.

```python
import matplotlib.pyplot as plt

## Identify the points on the chart
## Plot then show the chart
x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]
plt.plot(x, y)
plt.show()

## Add a legend to the chart
x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]
legend = ["January", "February", "March", "April"]
plt.xticks(x, legend)
plt.plot(x, y)
plt.show()

## This time a bar chart
x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]
plt.ylabel("Sales in USD")
plt.xlabel('Things')
plt.title("Monthly Sales")
plt.bar(x, y)
plt.show()
```
The `show()` method shows the specified chart.

## Modules: Requests

To make HTTP requests in Python, you need a requests module.

```python
import requests

response = request.get("https://www.google.com")

print(response.code)
print(response.headers)
print(response.text)
```

If you get a status code 200, you know things worked.

The response payload for the request is in the `response.text`, which is string. This is typically going to be XML or JSON.

JSON (JavaScript Object Notation) is a popular data serialization format. We can expect to get lots of data in JSON.

```python
## Call a REST API and pull back a JSON document
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
stuff = requests.get(url)
stuff.json()["title"]
```

```python
## Call a REST API and pull back a collection of JSON documents
import requests

url = 'https://jsonplaceholder.typicode.com/posts/'
stuff = requests.get(url)
for thing in stuff.json():
    print(thing["title"])
```

## Modules: json

Programmers can work with JSON in Python with the `json` module:

```python
import json, requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response_in_json = requests.get(url)
response_as_object = json.loads(response_in_json)
```

In the above, we've called a REST method. The call returned a JSON payload. We turned the payload into a dictionary object with `json.loads()`.

You can turn a dictionary into a JSON string with `json.dumps()`:

```python
my_object = { ... }

json.dumps(my_object)
json.dumps(my_object, indent=4, sort_keys=True)
```

 You can pretty print a dictionary with the `pprint` module's `pprint()` method:

```python
import pprint as pp

some_dictionary = { ... }

## Prints a formatted version of the dictionary
pp.pprint(some_dictionary)
```

## Modules: pyodbc

You can use the pyodbc module to make ODBC connections to various relational database systems:

```python
## Connect to the local SQL Server database and retrieve data
from pyodbc import connect

db_connection_string = r'Driver={SQL Server};Server=(local);Database=tempdb;Trusted_Connection=yes'
db_connection = connect(db_connection_string)

command = db_connection.cursor()
command.execute("SELECT name FROM sys.databases")

while 1:
    row = command.fetchone()
    if not row:
        break
    print(row.name)

db_connection.close()
```

This follows the typical string, connection, command, and fetch logic of most connection libraries.

## Modules: Pandas

There are several Python modules available for working with Excel files. The following examples use Pandas and xlrd. Pandas is an open source library (module) for data manipulation and analysis. *xlrd* is a module for reading and manipulating Microsoft Excel spreadsheets.

Install Pandas with the following:

```sh
pip3 install pandas
pip3 install xlrd
```
**NOTE**: Examples include an Excel spreadsheet named `sales.xlsx`. Spreadsheet has two tabs: sales and customers.

Pandas

```python
#!/usr/bin/env python3

import pandas as pd

workbook = pd.ExcelFile("sales.xlsx")

## Print out the sheet names in the workbook
print("Printing the names of the sheets in the workbook")
print(workbook.sheet_names)

## Create an object for the `Sales` worksheet
sales = workbook.parse("sales")

## Print the contents of the sales workbook
print(sales)

## Display all data in the `Date` column
print(sales.Date)

## Print the sum of all sales
print(f"The sales total is ${sales.Amount.sum()}")

## Print the 2nd row in the data set
print(sales.loc[1])
```

You can filter the dataset by value. For example, lets say you want to see all the sales for more than $1,800:

```python
## Sales for more than $1,800
sales.loc[ sales['Amount'] > 1800 ]

## A list of customers with sales over
## the specified amount
sales.loc[ sales['Amount'] > 1800 ]['Customer'].unique()
```

You can also search a dataframe for a specified value. For example, let's say you want to search for customer transactions by name:

```python
## Step-1: Creating an index on customer first
sales.set_index("Customer", inplace=True)

## Step-2: Searching for sales by customer
print(sales.loc["MMC Inc."])
```
We're creating an index on `Customer` then using that index to find records with a specific customer.
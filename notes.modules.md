# Python Modules

Modules are `py` files imported into other scripts and/or modules.

## Documenting a Module

Documentation is captured in docstrings. Comments need to follow the format described in [Google's Python Style guide](http://google.github.io/styleguide/pyguide.html).

```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an overall description of the module or program.  Optionally, it may also contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

The docstring of a module can be found in it's "__doc__" attribute.

## Running a Module Like a Script

Module can be run independently just like scripts. To create a module that can be run like script, check the value of the `__name__` variable. If the variable's value is "__main__", the module was run from the commandline.

In the body of your script, include the following conditional:

```python
if __name__ == '__main__':
    do-script-body
```

"do-script-body" is what happens when the module is run from the commandline.

## Importing a Module

The following commands imports a module:

```python
## Option-1: Import a Module
import <file_name_without_file_extension>

import math
math.factorial(10)
```

The following creates a public name `math` and maps the `math` module to it. The objects inside the module are still private, and they can only be accessed through the `math` object.

```python
## Option-2: Import Specific Function
from <module> import <function>, <function>

from math import factorial, assign
factorial(10)
```

This imports the names specified into the public scope. After this, <function> and <function> can be accessed from with-in the function.

```python
## Option-3: Import Specific Function Under a Different Name
from <module> import <function> as <alias>
```

The following commands import functions and objects from a script:

```python
## Import all code from a file
from <file_name_without_file_extension> import *
```

This is a little tricky. Python includes a list variable named `__all__`. `__all__` contains the names of objects to export when the module is loaded with `import *`. 

* If `__all__` has values, this statement imports the names referenced in `__all__`.
* If `__all__` has no values or is undefined, this statement imports everthing except names starting with an underscore.

```python
## Imports single class from specified file
from <file_name_without_file_extension> import <class_name>
t = <ClassName>()
```

You can list the modules on your system with `help('modules')`.

## Reloading Modules

Modules can be reloaded with the `reload()` function from the `importlib` module:

```python
import pandas
import importlib

importlib.reload(pandas)
```

## Projects

Projects are a mechanism for organizing large collections of relate modules. Think of packages as directories on a file system. Think of modules like files within the directories. A package is nothing more than a directory hosting a __init__.py file. Packages contain modules.

* All packages are modules, but not all modules are packages.
* Packages can contain modules or packages (sub-packages).
* There are two types of packages: regular and namespace.

You'll always import modules, not packages; for example:

```
foo/
  __init__.py
  one/
    __init__.py
  two/
    __init__.py  
  three/
      __init__.py
```   
   
```python
## executes foo/__init__.py and foo/one/__init__.py
import foo.one

## executes foo/two/__init__.py
import foo.two

## executes foo/three/__init__.py
import foo.three
```

When a module with-in a package is imported, the code in the package's `__init__.py` file is executed. `__init__.py` can contain any Python code.

Developers can import names from a project using `from <project> import *`. This will import the names referenced in `__all__`. `__all__` is a list defined in the module's `__init__.py` file. If `__all__` hasn't been created, `import *` does not import anything.

With respect to `__init__.py`:

* It can be blank.
* Is optional as of Python 3.3; although, it's a best practice to include.
* Tells developers they're looking at a project directory.
* Executes as a package.

## Project Layout

The following is recommended Python project layout:

project
	docs/
	src/
		package_name/
			__init__.py
			module1.py
			module1.py
	tests/
	README (md or rst)

* *docs*, hosts the documentation for your application.
* *tests*, contains the various unit tests for your solution. You typically want to keep your tests separate from the code you plan to package and deploy.
* *src*, your source code. `src` typically contains a package directory, which is named after your project.

Your READ ME should be written for people first being introduced to your project.

## Building a Project

There are a variety of ways to deploy a Python solution. You can share a script. You can deliver an executable zip file. But, for packages and modules, the standard approach is to create a distribution package.

There are two types of distribution packages:

1. Built Distributions: 
	1. Deployed to a Python installation directory
	1. All steps to build the project have been completed 
	1. Can be platform specific
2. Source Distributions: 
	1. Contains everything needed to build the package
	1. Package needs to be built before being installed
	
### Built distributions

This is the more common of the two build distributions. It's also the recommended distribution option.

Built distributions employ a distribution format. There are a variety of formats. The most common of these formats is `wheel`. To use the wheel format, you start by installing the `wheel` module:

```sh
pip install wheel
```

You can then create a distribution package by running setup with  bdist_wheel.

```sh
python setup.py bdist_wheel
```

This will create a "dist" directory. Inside the "dist" directory will be your distribution package.

You can install the package with pip:

```sh
pip install thinger-1.0.0-py3-none-any.whl
```

Notice the distribution package file's name includes the `.whl` extension. The name indicates the (a) version of Python, (b) binary interface (ABI), and (c) platform the package will work with.

### Source Distributions

Source distributions aren't employed as frequently as built distributions.

You create a source distribution with the following:

```sh
python setup.py sdist
```

This will create a "dist" directory containing your distribution package. The distribution package will be a compressed tarball, which you can install with pip.

## Deploying a Distribution Project

Cool kids deploy projects to Python Package Index services. The most popular of these services is `pypi.org`. `pypi.org` is a free public service anyone can take advantage of. Think of it like npmjs.org.

Once you've created an account at pypi.org, you can upload your distribution package with the `twine` module.

 ```sh
 python -m pip install twine
 
 twine upload <package-name>
 ```

After calling `twine`, you'll be prompted for your pypi.org credentials, authenticate, and start uploading the package (assuming you authenticated successfully).

After you've uploaded your package, you can access from the pypi.org website.

## Plugins

Python supports a feature named "plugins", which lets you extend a project with additional modules. The extensions (modules extending the package's functionality) exist outside the package. You define extension points with-in your package. Modules can then be created that match that extension point.

You can implement packages using one of two mechanisms:

* Namespace Packages and the pkgutil module
* Entry point functionality of SetupTools



# Modules: OS

The OS module controls things on the host. For example, you can use the OS module to execute shell commands care-of the `system()` method:

```Python
import os

## On windows...
os.system('CLS')

## On MacOS
os.system('clear')
```

# Modules: Time

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

# Modules: Matplotlib

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

# Modules: Requests

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

# Modules: json

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

# Modules: pyodbc

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

# Modules: Pandas

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
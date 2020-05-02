# Python Notes

## Language Background

1. Python is an open source project managed by the not-for-profit Python Software Foundation.
2. Python versions for Windows, MacOS, and Linux flavors
    1. can be downloaded from https://www.python.org/downloads.
3. There are several types of Python (e.g., J-Python, PyPy, C-Python, etc.)
    1. *CPython (most common), written in C, runs on everything, and considered the reference implementation
    2. Jython, written in Java runs on JVM
    3. IronPython, (Python 2.x ONLY) written in C# and integrates with .NET
    4. PyPy, written in RPython
4. Two main branches of Python: 2.7 and 3.x.
    1. The 2.x branch is depricated 
    2. 3.x branch is under active development; use for new projects.
5. Scripts are saved with the ".py" file extension.
6. Standard library documentation is available at Python.org
7. *Python enhancement proposals* (PEPs) are where enhancement requests are made.
    1. PEP 8: Describes how you should format your code.
    2. PEP 20: Describes the guiding principals of Python.
        1. You can see this from the REPL by typing `import this`.
8. Pythonic style: simplicity, readability, and expressiveness
    1. Never mix spaces and tabs
    2. Two blank lines between functions
    3. Indent 4 spaces; Indent after a colon (:)    

## Language Reference

Python ships with an interface: **REPL**:

1. REPL is an acronym for Read-Evaluate-Print-Loop
2. REPL is an interactive shell where programmers entered commands.
3. With-in the REPL, `_` shows the last returned value.

Python is case sensitive. It uses indentation to delineate code blocks (vs. brackets).

### Code Documentation and Comments

Python differentiates between documentation and comments. Documentation is placed in docstrings. A **docstring** is implemented as a triple quote: 

```python
'''
There is documentation in here some place.
'''
```

These should be at the start of a function or module. You can create code comments with the hash. Sort of like `Get-Help` in PowerShell, you can call `help()` in Python to see documentation for a module or function:

```python
import <module>

help(<module>)
help(<module>.<function>)
```

...for example...

```python
import math
help(math)
```

Comments need to follow the format described in [Google's Python Style guide](http://google.github.io/styleguide/pyguide.html).

```python
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an overall description of the module or program.  Optionally, it may also contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

```python
def whatevs(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from
    the Table instance represented by big_table. 
    Silly things may happen if other_silly_variable
    is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key
            of each table row to fetch.
        other_silly_variable: Another optional variable,
            that has a much longer name than the other 
            args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table 
        row data fetched. Each row is represented as a
        tuple of strings. For example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from
        the dictionary, then that row was not found in
        the table.

    Raises:
        IOError: An error occurred accessing the 
        bigtable.Table object.
    """
```
Use code comments to explain why you've taken a specific approach. Code comments use hashes like Bash or Powershell.

```python
## This is my lame comment
def thinger():
    print("Fun!")
```

### Variables and Primitve Types

Python is not an "aesthetically typed language", programmers don't assign variables when declaring like PowerShell or Perl.

```python
name = 'sabrina'
```

There are four scopes:

1. local
2. enclosing
3. global
4. built-in

Python determines type based on a variable's value or optional declaration. There are four primitive types:

1. Integer an integer
1. Float: machine level double precision floating point numbers
1. Byte: an array of bytes
1. Complex: machine level double precision floating point numbers
1. String: sequence of values that represent Unicode code points
1. Boolean: values are true and false

Float and complex number inherit the host's and C's or Java's accepted range and handling of overflow. There is no `char` type in Python.

* **Type hinting** is something developed for IDEs. It tells them a parameter or function's return type.

```python
def add_numbers (a: int, b: int) -> int:
    return a+b
```

Undefined values initialize to `None` the default value for variables.
It represents the absence of a value, and it can be assigned and evaluated.

```python
var = None

if var is None:
    print("yes")
```

In CPython, `id()` shows the memory address for a given variable.

In all distributions of Python, you can determine a variable or property's type using the `type()` function.

```python
## The following returns the type of a given variable
type(<identifier_name>)
type(<identifier_name>.<identifier_name>)
```

Boolean variables equate to `True` and `False`, capitalization matters here. Python interprets variable values as truthy and falsy as follows:

```python
## Evaluate to False
bool(0)
bool([])
bool("")
bool(False)

## Evaluate to True
bool(anything not 0)
bool("False") # A string of any value
bool([1, 2, 3])
bool(True)
```

You can cast variables from one type to another using the type cast functions:

```
int()
str()
float()
```

...for example...

```python
## Cast a float to an integer
value = 3.1
int(value) == 3
```

#### Strings and Bytes

String are immutable sequences of unicode code points.


```Python
my_name = "john scena"
```

Strings can be wrapped in single and double quotes as well as triple-double quotes

```python
'Test'
"Test"
"""Test"""
```

New lines are represented as "\n" in Python on all platforms: Universal New

You can also create raw strings. These are strings that don't respect escape characters:

```python
raw = r'this is a raw string'
```

Like in Java, strings are objects in Python with a rich set of methods: 

```python
## You can parse a comma seperated string with the split() method
<string>.split()

## Change the case of text to upper case
<string>.capitalize()
```

Python supports string interpolation in one of two ways:  

```python
## Old Way
"I like to eat {0} on {1}.".format('ramen', 'Tuesday')

## New Way
like_what = 'ramen'
like_what_when = 'Tuesday'

f"I like to eat {like_what} on {like_what_when}."
```

Bytes are sequences of bytes used for raw binary data or fixed width single byte encoding.

```python
thing = b'my data I want to store as bytes'
```

`bytes` support indexing (like in an array or string) and splitting. You can convert a string stored as a byte into a string provided you can specify the encoding:

```python
thing = b'my data I want to store as bytes'
decoded = thing.decode('utf8')

stuff = 'more stuff I want to store'
stuff_byte = stuff.encode('utf8')
stuff
```

*NOTE*: http responses are transmitted as byte streams.

### Lists

Lists are a sequence of objects like arrays in other languages. Lists are mutable, you can replace, add, and remove elements. List assignment sytnax is as follows:

```Python
## Assigning an empty list
team = []

## Assigning a static list
team = ['adam', 'steve', 'charles']

## Assigning a static list (mixed data types)
team = ['adam', 3, False, 2.17]

## Replacing an element in an existing list
team[1] = 'stephen'

## Adding to an existing list
team.append('gowthom')

## You can close a list with a comma.
stuff = [1, 2, 3, 4, ]
```

Although not recommended, you can have multiple types in a single list. There is even a list construtor, which creates lists from other things like strings:

```python
## Creates a list with an element per character
list("this is my thing")
```

List indexes are 0 based. The following is the value retrieval syntax:

```python
## retrieve second item in list
team[1]

## Gives us the last item in the list
team[-1]

## (List slicing) gives us a portion of the list
team[<start_element>:<end_element>]

team[1:]
team[1:-1]
```

### Dictionaries

Dictionaries allow storing of key-value pairs. These synonymous with maps or associative arrays in other languages or objects in JavaScript.

```python
## Simple Dictionary
team_member = { "name" : "Adam" }

## Complex Dictionary
team_member = {
        "name" : "Adam",
        "bag" : {
            "token" : 1,
            "is_blue" : "no"
        }
    }
```

Data retrieval follows the following syntax:

```python
## Retrieve the value for a key
team_member["name"]

## Get a nested dictionary value
team_member["bag"]["token"]

## Delete a key/value
del team_member["name"]

## Returns 'unknown' if the key 'name' can't be found
team_member.get("name", "unknown")

## Returns all keys and values respectively
team_member.keys()
team_member.values()
```
We can remove items with the `del` command:

```python
del team[2]
```

You can get the size of a list with `len(team)`.

### Tuples

```python
## Immutable
tuple = (1, 2, 3, 'a')
```

### Sets

```python
## Returns a relational set
set([3, 2, 1, 1])
```

### Ranges

Range values

```python
## Creates a range object from 0 to 10
range(10)

## Creates a range object from 1 to 10
range(1, 10)

## Creates a range object from 1 to 10 by 2's 1, 3, 5
range(1, 10, 2)
```

### Functions

A function is collection of commands referred to by a name. Syntax for declaring and referencing a function is as follows:

```Python
## Declare thinger()
def thinger(stuff):
    def otherthinger(morestuff):
        return 1
    something = otherthinger(2)
    print("something")

## Call thinger()
thinger(1)
```

If a function doesn't provide an explicit return value, it returns `NONE`.

**[!] STYLE:** Separate functions with two spaces. Separate sections of code with a single space.

The following is the syntax to declare a function:

```python
## Defining a function with no parameters
def <function_name>():
    body_of_function
    return <return_value>


## Defining a function with two parameters
def <function_name>(<param1>, <param2>):
    body_of_function
    return <return_value>


## Defining a function with a parameter having a default value
def <function_name>(<param1> = <def_value>):
    body_of_function
    return <return_value>


def fn(name):
    teams = []
    teams.Append({ "name" : name })

    return teams
```

A function can take a list as a parameter with the following syntax:

```python
## "*args" Creates a list object
def fn(name, *args):
    print(name)
    print(args)

## You don't include the astrisk when you call the function
fn ('adam', 'billy', 'mike', 'spence')
```

A function can take a dictionary as a parameter with the following syntax:

```python
## Creates a dictionary argument
def fn(**kwargs):
    print(kwargs["thing"])
```

Lambda functions are used in functions that take other functions as an argument

* Also called anynonymous functions
* Can accept any number of arugments but only have one expression
* Lambda functions have an implicit return, returning the result of the expression

```python
## Lambda Functions (Annonymous functions)
<function-name> = lambda <param1>, <param2>: <expression>
<function-name>(<param1>, <param2>)

## Function expressed as a lambda function
double = lambda x: x * 2
double(3)

'''...or...'''

(<param1>, <param2>: <expression>)(<param1>, <param2>)

## You are not binding the function to a name
(lambda x, y: x + y)(5, 3)

'''...or...'''

>>> def NumOfThings(n):
...     return lambda p1: n + p1

## You actually assign the lambda function to the variable
>>> my = NumOfThings(2)
>>> my(2)
4
```

### Exception Handling

Error handling in Python is handing through a `TRY CATCH` statement with syntax:

```python
student = { 'b' : 123 }

## Catch any error and execute the handler
try:
    last_name = student['a']
except Exception:
    print('Error accessing student name')

## Catch any error, and execute the hander, which 
## prints an error message
try:
    last_name = student['a']
except Exception as error:
    print(error)

## Catch either a key error or generic exception, each with
## their own handler
try:
    last_name = teacher['a']
except KeyError:
    print('Error accessing student name')
except Exception:
    print("Something happened. I'm just a *@#$ that likes big @&#@.")
```

### Extensibility - Modules and Packages

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

### Managing Your Python Environment

Python includes a feature named **virtual environments**.

```Bash
# Verify the version of Python in your PATH
Python --Version

# Install a module using PIP
pip install <module>

# Upgrade PIP to the latest version
pip install --upgrade pip`

# Check your virtual environment
virtualenv <environment_name>

## Run a Python script
python <script_name>
```

### Expressions and Conditional Logic

Python implements the following comparison operators:

```Python
<var> == 3                          ## Equal to
<var> != ''                         ## Not equal to
<var> == 3 and <var> != 2           ## Logical AND
<var> == 3 or <var> != 2            ## Logical OR
"adam" in team                      ## Determines if a value is in a list
not <expression>                    ## Express Not Evaluate to True
```

Python's `if-elif-else` syntax is as follows:

```python
if <expression>:
    do-something
elif <expression>:
    do-something
else:
    do-something
```

Here is an example:

```python
number = 2

if number == 2:
    print('Yes')
```

In the same sphere as the `if` statement is the terniary operation:

```python
<true-condition> if <expression> else <false-condition>

'larger' if a > b else 'smaller'
```

### Loops

Python has three types of loops:

* For-Each
* For
* While

Execution sytax for each loop is as follows:

```Python
## For-Each Loop
for <obj> in <list>:

t = ['adam', 'billy', 'suzie']
for each i in t:

## For Loop
for i in range(10):

## While Loop
while a < 10:
    a++

## There is no do...while loop in Python.
## Developers use breaks to mimic that flow
while 1 == 1:
    do-something

    if done == True:
        break

## Stops the loop from executing
break

## Continues the loop without running this iteration
continue
```

### Classes

```Python
## The 'pass' keyword tells python to do nothing.
## It's usable in functions as well.'''
class Student:
    pass

class door:
    state = closed

    ## Constructor
    def __init__(self, state)
        self.state = state

    ## Called when casted to a string like in print()
    def __str__(self)
        return "Student"

    ## The 'self' parameter is always passed. It allows the
    ## method to reference itself
    def open_door(self):
        self.state = 'open'
        return self.state

## First way to set a private data member
class Student:
    ## Static value
    school_name = 'Springfield Elementary'

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

        students.append(self)

## Second way to set a private data member
class Student:
    def set_name(name):
        this.name = name

## One way to call a static data member
Student.school_name

## Create a child class 'HighSchoolStudent' from 'Student'
class HighSchoolStudent(Student):
    school_name = 'greenfield'

## You can override methods by just entering the method with same signature
## in your child class.
def parent_method():
    orig_value = super().parent_method()
    return orig_value + 'HS'

## You can inherit several Classes
## There are no public/private data members in your class
def <function_name>():
    """
    Comment block
    """
```

### File Access

There are five file access modes:

* w, writing (will overwrite anything in the file; file does not need to exist)
* r, reading (requires file to exist)
* a, append
* rb, reading a binary file
* wb, writing to a binary file

These describe the method Python will use to read or write from a file.

```python
## Opens a file
file = open('deezCherries.txt', 'a')

for line in file.readlines():
    ## ...do something...

## Closes the file (prevents memory leaks)
file.close()
```

File access makes use of these things called generator functions, which leverage the yield operator:

```python
## This is a function that uses a generator
def read_file():
    try:
        file = open('file.txt', 'r')

        ## Uses the generator
        for line in read_students(file):
            Print(line)

        file.close()
    exception Exception:
        print('boom')

## Defines the generator
def read_students(file):
    for line in f:
        yield line
```

### Scripts

You know what a script is, or should. Python scripts carry the "py" file extension. Just remember on Linux and MacOS, you have to permission the file as executable:

```sh
chmod u+x foo.py
```

Scripts should include a shebang at the top

At the top of your scripts, you want to include a shebang:

```python
#!/usr/bin/env python3
```

This does a few things:

* Determine's the script's ability to be run as a standalone executable; running the script without calling python passing the script's full path
* Tells whoever opens the script what they're looking at e.g., Python script, shell script, etc. 

The example shebang employs `env`, which finds the specified executables in your path. In the case of the example shebang, it finds the `python3` executable.

Windows distributions of Python ship this thing called PyLauncher. **PyLauncher** parses the shebang to determine which version of Python to compile and run the script with.

The `__name__` has one of two values in scripts:

* "__main__" if the script was called from the command line.
* The name of it's script, if it's script was imported into an another script.

If you want a script to be executable as well as importable, you can use the following to conditionally run the script's body:

```python
if __name__ == '__main__':
    do-script-body
```

Scripts and modules imported into a script are only executed once, on first import.

### Virtual environments

```python
## Setting up a virtual environment
pip install virtualenv

## Create the environment
mkdir <env-name>
virtualenv <env-name>
virtualenv --python=<python_version> <env_name>
virtualenv --version

## activate the environment
source /
```

You can keep all virtual environments in a single folder.

### Flask

* Flask and DJango are web development frameworks.

```python
## Sample Flask script
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

# Frequently Asked Questions (FAQ)
(Q) How do I clear the session in the REPL?

Use the `system` method of the `os` module to run the `cls` command:
```Python
import os
os.system('CLS')
```

(Q) Can I use Python with .NET Libraries?

You can use IronPython. IronPython is a port of the Python programming language to the .NET framework. The following article talks about using IronPython to script the SMO library: [Using SMO to manage a MS SQL Database](http://www.ironpython.info/index.php?title=Using_SMO_to_manage_a_MS_SQL_Database).
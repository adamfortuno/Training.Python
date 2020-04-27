# Python Notes

## Language Background

1. Python is an open source project managed by the not-for-profit Python Software Foundation.
2. Python versions for Windows, OS X, and Linux flavors can be downloaded from https://www.python.org/downloads.
3. There are several types of Python (e.g., J-Python, PyPy, C-Python, etc.), C-Python (written in C) is generally considered the reference implementation.
    1. CPython (most common), written in C and runs on everything
    2. Jython, written in Java runs on JVM
    3. IronPython, (Python 2.x ONLY) written in C# and integrates with .NET
    4. PyPy, written in RPython
4. Two main branches of Python: 2.7 and 3.x. The 2.x branch is depricated while the 3.x branch is under active development. Future development should use 3.x.
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

1. Python ships with an interface named the **REPL** (Read-Evaluate-Print-Loop)
    1. REPL is an interactive shell where programmers entered commands.
    2. You can use `_` to see the last "_" value returned by the REPL.
2. **Python is case sensitive**.
3. Python uses indentation to delineate code blocks (vs. brackets).
4. Python is not an "aesthetically typed language", programmers don't assign variables when declaring.
    1. **Type hinting** is something developed for IDE's to help them know the type of a given parameter.
        ```python
        def add_numbers (a: int, b: int) -> int:
        return a+b;
        ```
5. `None` is a value that represents the absence of a value.
    1. It can be assigned and evaluated.
        ```python
        var = None
        if var is None:
            print("yes")
        ```
    2. `if bool(var)` will equal false.
6. A variable with a value will evaluate to true.
    1. The following are all false:
        ```python
        bool(0) 
        bool([])
        bool("")
        ```
    2. The following are true:
        ```python
        bool(anything not 0)
        bool("False")
        bool([1, 2, 3])
        ```
7. Although not recommended, you can have multiple types in a single list.
8. Dictionaries allow storing of key-value pairs `{ name: adam }`
9. Wrap statements in an exception handler when there is a potential of them failing.
10. Function permits nested declaration of functions:
    ```Python
    def thinger(stuff):
        def otherthinger(morestuff):
            return 1
        something = otherthinger(2)
        print("something")
    
    thinger(1)
    ```
11. Extensibility libraries appear in the form of modules.
    1. A Python **package** is a collection of modules.
    2. A Python **module** is a single python script hosting a collection of functions as a single unit.
    3. Python 3.x ships with a package manager named **pip**, which is a CLI program you can use to install pacakges.
        1. When you install a package using "pip", you do it from the CLI (not Python shell).
    4. By default pip retrieves packages from [PyPI (Python Package Index)](https://pypi.org/), which is a Python package repository.
        1. Packages on PyPI will link to the package's website.
    5. Sample package install: `pip install flask`.
13. In Python everything is an object (including modules and functions). Think of
    1. Python as named references to values.
    1. Assignment doesn't "place a value in a box" it puts a nametag on an item
    1. A given object can have multiple name tags (be referenced by two different names)
    1. Python garbage collector recycles objects with no reference
    1. id() function returns a unique and constant identifier
    1. "is" operator determines if two names point to the same object
1. Function arguments are passed by object reference
1. Functions return objects by reference

# Code

1. Python includes a feature named **virtual environments**.
  
### Managing Your Python Environment

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

### Loading Modules

* You can locate the name of a module in it's "__name__" attribute
* The docstring of a module/function can be found in it's "__doc__" attribute

```Python
'''Import a Module'''
import <file_name_without_file_extension>                       

import math
math.factorial(10)

'''You can import a specific set of functions from a module
from <module> import <function>, <function>
'''
from math import factorial, assign
factorial(10)

'''Imports a function with the name "<alias>"'''
from <module> import <function> as <alias>

'''Imports all code in a single file'''
t = <file_name_without_file_extension>.<ClassName>() 

'''Imports single class from specified file'''
from <file_name_without_file_extension> import <class_name>
t = <ClassName>()


'''Imports all code in a single file'''
from <file_name_without_file_extension> import *
t = <ClassName>()

'''Shows the functions associated with a module'''
dir(<identifier>)

'''Shows a module's or function's help page'''
import <module>
help(<module>)
help(<module>.<function>)

import math
help(math)
```

### Code Comments
    
* It's common to write comments in a trip-quote string (```'''```) with no assignment

```python
'''
This function does something fun.
'''

def thinger():
    print("Fun!")
```

### Variables

* Scopes are local, enclosing, global, and built-in.

```Python
'''Type hinting ,like `name: string` tells an IDE the expected type for a given parameter'''
def boss_him(name: string) -> string
    return name + ' beeping boss'
```
Other stuff
```Python
'''Cast a float to an integer'''
value = 3.1
int(value) == 3

'''Python uses 'None' and undefined in lieu of $Null. In the following 'is_sucker' is None'''
is_sucker = None 

'''The following is not defined, which is different than None'''
is_not_sucker

'''The following returns the type of a given variable'''
type(<identifier_name>)
type(<identifier_name>.<identifier_name>)
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

#### Variables: Strings

String are immutable sequences of unicode code points. They are implemented as objects, like Powershell and Java, and they  have a rich set of methods ot maniuplate their value.

New lines are represented as "\n" in Python on all platforms: Universal Newline Support. You can escape a charcter in Python using the backslash.

You can also create raw strings. These are strings that don't respect escape characters:

```python
raw = r'this is a raw string'
```

```Python
my_name = "john scena"

'''Strings can be wrapped in single and double quotes as well as triple-double quotes'''
'Test'
"Test"
"""Test"""

'''You can parse a comma seperated string with the split() method'''
<string>.split(',') 

'''Change the case of text to upper case'''
<string>.capitalize()

'''To see a full list of functions, see 'str' help page'''
help(str)

'''Interpolation in Python'''
"I like to eat {0} on {1}.".format('ramen', 'Tuesday')

like_what = 'ramen'
like_what_when = 'Tuesday'
f"I like to eat {like_what} on {like_what_when}."
```

#### Variables: Boolean

Boolean values in Python are case sensitive e.g., `True` not `true`.

```Python
IsGreat = True
IsHorrible = False

'''The following are all false:'''
bool(0) 
bool([])
bool("")
bool(False)

'''The following are true'''
bool(anything not 0)
bool("False")
bool([1, 2, 3])
bool(True)
```
### Lists

```Python
'''List assignment'''
team = []                               '''Empty list'''
team = ['adam', 'steve', 'charles']     '''static list'''
team[1] = 'stephen'                     '''replace item in list'''
team.append('gowthom')	                '''Add an item to a list'''

'''List retrieval'''
team[1]                                 '''retrieve second item in list'''
team[-1]                                '''Gives us the last item in the list'''
team[<start_element>:<end_element>]     '''(List slicing) gives us a portion of the list'''
team[1:]				
team[1:-1]

len(team)                               '''Gives me the length of a list'''
del team[2]                             '''Deletes the third element (lift shifts left)'''

stuff = [1, 2, 3, 4, ]                  '''You can close a list with a comma.
```

### Dictionaries

```Python
'''Creating dictionaries'''
team_member = { "name" : "Adam" }
team_member = { "name" : "Adam", "bag" : { "token" : 1, "is_blue" : "no" } }

team_member["name"]                 '''Get a dictionary value for a given key'''
team_member["bag"]["token"]         '''Get a nested dictionary value'''
del team_member["name"]

.get("name", "unknown")             '''Returns 'unknown' if the key 'name' can't be found'''
.keys()                             '''Returns all keys'''
.value()                            '''Returns all values'''

'''List types'''
tuple = (1, 2, 3, 'a')              '''Immutable'''
set([3, 2, 1, 1])                   '''Returns a relational set'''

'''Range of values'''
range(10)                           '''Creates a range object from 0 to 10'''
range(1, 10)                        '''Creates a range object from 1 to 10'''
range(1, 10, 2)                     '''Creates a range object from 1 to 10 by 2's 1, 3, 5'''
```

### Expressions

```Python
'''Comparison operators'''
<var> == 3                          '''Equal to'''
<var> != ''                         '''Not equal to'''
<var> == 3 and <var> != 2           '''Logical AND'''
<var> == 3 or <var> != 2            '''Logical OR'''
"adam" in team                      '''Determines if a value is in a list'''
not <expression>                    '''Express Not Evaluate to True'''

'''If-Blocks take the form'''
number = 2
if number == 2:
    print('Yes')

if <expression>:
    do-something
elif <expression>:
    do-something
else:
    do-something

'''Terniary operation in Python'''
<true-condition> if <expression> else <false-condition>
'larger' if a > b else 'smaller'        
```

### Loops

```Python
'''General structure of a foreach loop in Python'''
for <obj> in <list>:

t = ['adam', 'billy', 'suzie']		
for each i in t:

'''Runs a loop from 0 to 10'''
for i in range(10):

'''Stops the loop from executing'''
break

'''Continues the loop without running this iteration'''
continue

while a < 10:
    a++

'''There is no do...while loop in Python. Developers use breaks to mimic that flow'''
while 1 == 1:
    do-something
    if done == True:
        break
```
### Exceptions

```Python
'''Basic exception handling with a try..catch block'''
student = { 'b' : 123 }
try:
    last_name = student['a']
except KeyError:
    print('Error accessing student name')

'''Prints information about the error'''
try:
    last_name = student['a']
except Exception as error:
    print("Something happened. I'm just a *@#$ that likes big @&#@.")
    print(error)

try:
    last_name = teacher['a']
except KeyError:
    print('Error accessing student name')
except Exception:
    print("Something happened. I'm just a *@#$ that likes big @&#@.")
```

### Functions

* The name of a function can be found in it's "__name__" attribute
* There must be two spaces between functions
* Lambda functions are used in functions that take other functions as an argument

```Python
def <function_name>(<param1>, <param2>):
    body_of_function

def <function_name>(<param1> = <def_value>):

def fn(name):
    teams = []
    teams.Append({ "name" : name })
    return teams


def fn(name, *args):                        '''"*args" Creates a list object'''
    print(name)
    print(args)                             '''Note, don't use the astrisk'''

fn ('adam', 'billy', 'mike', 'spence')

def fn(**kwargs):                           '''Creates a dictionary argument'''
    print(kwargs["thing"])
```

### File Access

* Access modes
    * w, writing (will overwrite anything in the file; file does not need to exist)
    * r, reading (requires file to exist)
    * a, append
    * rb, reading a binary file
    * wb, writing to a binary file

```Python
file = open('deezCherries.txt', 'a')        '''Opens a file'''
for line in file.readlines():
    '''do something'''
file.close()                                '''Closes the file (prevents memory leaks)'''

'''Generator Function (using the yield operator)'''
def read_file():                            '''This is a function that uses a generator'''
    try:
        file = open('file.txt', 'r')
        for line in read_students(file):    '''Uses the generator'''
            Print(line)
        file.close()
    exception Exception:
        print('boom')

def read_students(file):                    '''Defines the generator'''
    for line in f:
        yield line
```

### Lambda Functions

* Also called anynonymous functions
* Can accept any number of arugments but only have one expression
* Lambda functions have an implicit return, returning the result of the expression

```Powershell
'''Lambda Functions (Annonymous functions)'''
<function-name> = lambda <param1>, <param2>: <expression>
<function-name>(<param1>, <param2>)

double = lambda x: x * 2                    '''Function expressed as a lambda function'''
double(3)

'''...or...'''

(<param1>, <param2>: <expression>)(<param1>, <param2>)

(lambda x, y: x + y)(5, 3)                  '''You are not binding the function to a name'''

'''...or...'''

>>> def NumOfThings(n):
...     return lambda p1: n + p1        

>>> my = NumOfThings(2)                     '''You actually assign the lambda function to the variable'''
>>> my(2)
4
```

### Classes

```Python
''' The 'pass' keyword tells python to do nothing. '''
''' It's usable in functions as well.'''
class Student:
    pass

class door:
    state = closed

    def __init__(self, state)               ''' Constructor '''
        self.state = state

    def __str__(self)                       ''' Called when casted to a string like in print() '''
        return "Student"

    def open_door(self):                    ''' The 'self' parameter is always passed. It allows the '''
        self.state = 'open'                 ''' method to reference itself '''
        return self.state

''' First way to set a private data member '''
class Student:
    school_name = 'Springfield Elementary'  ''' Static value '''

    def __init__(self, name, student_id):   
        self.name = name
        self.student_id = student_id
        
        students.append(self)

''' Second way to set a private data member '''
class Student:
    def set_name(name):
        this.name = name

''' One way to call a static data member '''
Student.school_name                         

''' Create a child class 'HighSchoolStudent' from 'Student' '''
class HighSchoolStudent(Student):
    school_name = 'greenfield'

''' You can override methods by just entering the method with same signature '''
''' in your child class. '''
def parent_method():
    orig_value = super().parent_method()
    return orig_value + 'HS'

''' You can inherit several Classes '''
''' There are no public/private data members in your class '''
def <function_name>():
    """
    Comment block
    """
```

### Flask

* Flask and DJango are web development frameworks.

```Python
''' Sample Flask script '''
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```
### Virtual environments

* No issue with keeping all virtual environments in a single folder

```Python
''' Setting up a virtual environment '''
pip install virtualenv

''' Create the environment '''
mkdir <env-name>
virtualenv <env-name>
virtualenv --python=<python_version> <env_name>
virtualenv --version

''' activate the environment '''
source /
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
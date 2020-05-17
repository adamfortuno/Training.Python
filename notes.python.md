# Python Notes

## Background

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
7. *Python enhancement proposals* (PEPs) are Python enhancement requests.
    1. PEP 8: Describes how you should format your code.
    2. PEP 20: Describes the guiding principals of Python.
        1. You can see this from the REPL by typing `import this`.
8. Pythonic style: simplicity, readability, and expressiveness
    1. Never mix spaces and tabs
    2. Two blank lines between functions
    3. Indent 4 spaces; Indent after a colon (:)
    4. Empty code blocks are not allowed in Pythin

## Installing Python

In the following, you'll install Python then check the version of Python. Check the version of Python after installation to make sure (a) Python is in the path and (b) you have the right version.

On MacOS, install Python3 via `brew`:

```bash
brew install python3
Python3 --version
```

MacOS ships with Python 2.x by default. You're installing Python3. Everything will have a "3" suffix: `python3` and `pip3` and `ipython3`.

## Installing and/or Upgrading PIP

You can install modules with pip using the following sytnax:

```bash
pip3 install <module>
pip3 install ipython3 # this example installs ipython3
```

You can upgrade pip with the following:

```bash
pip3 install --upgrade pip
```

## The REPL

Python ships with an interface: **REPL**:

1. REPL is an acronym for Read-Evaluate-Print-Loop
2. REPL is an interactive shell where programmers entered commands.
3. With-in the REPL, `_` shows the last returned value.

Python is case sensitive. It uses indentation to delineate code blocks (vs. brackets).

## Code Documentation and Comments

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

The line continuation character is the backslash, `\`:

```python
def console_card_printer(passenger, seat, flight_number, aircraft):
    output= f"| Name: {passenger}" \
            f"  Flight: {flight_number}" \
            ...
```

You can't have an empty code block in Python. If you need to create a code block without any logic, you have to include the `pass` keyword there. The following are some example of it in practice:

```python
## Using `pass` in a function
def foo:
    pass

## Using `pass` in a class definition
class Student:
    pass

## Using `pass` in an if-else statement
things = 12

if things > 0 and things <= 10:
    pass
elif things > 10 and things <= 20:
    print("Warmer!")
elif things > 20:
    print("Hot!")
```

## Variables: Primitves

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

## Variables: Strings and Bytes

String are immutable sequences of unicode code points.

```Python
my_name = "john scena"
```

We say they're immutable because you can't modify a string in place.

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

You can concatenate a string with the plus operator:

```python
str1 = 'this'
str2 = 'that'
str1 + str2
```

To join a large number of strings, use the `join()` method of the string class because its more efficent. The method inserts a separator into a collection of strings. You would pass the list of strings you want to join into join as a list of strings.

```python
<string>.join(<list_of_strings>)
''.join([str1, str2])
```

The partition method returns a tuple.

```python
<string>.partition('delimiter')
first, delimiter, second = <string>.partition('delimiter')
first, _, second = <string>.partition('delimiter')
```

*NOTE:* There is an unwritten convention where underscores represent un-used or un-wanted values.

## Structures: Lists

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

 1,  2,  3,  4,  5
-------------------
 0,  1,  2,  3,  4
-5, -4, -3, -2, -1

l[2] == 3
l[-2] == 4

The following is the value retrieval syntax:

```python
## retrieve second item in list
team[1]

## Gives us the last item in the list
team[-1]
```
List slicing gives us a portion of the list. Slicing follows the following format:

```python
team[<start_element>:<end_element>]
```

...for example...

```python
t = [1 , 33, 2, 32, 12]

## 3rd to 4th element
t[1:3]

## 4th element to end
t[3:]

## Everything up to 3rd element
t[:3]

## Last element in the lsit
t[-1]

## All elements
t[:]
```

The following are ways to do a shallow copy of a list:

TBA - Shallow copy a list

A shallow copy creates a new list; however, items in that list reference the same objects as the prior list.

To do a deep copy, use the `copy()` method from Python's standard library.

```python
list_object = [ 'fox', 'dog', 'cat', 'bat']

## Add an item to the end of the list
list_object.append('nat')

## Insert an element into at the specified index
list_object.insert(<index>, <value>)

## Returns the index for the first occurrence of `dog`
list_object.index('dog')

## Pop the last item from the list
list_object.pop()

## Pop the specified item from the list
list_object.pop(3)

## Remove element 2
del list_object[2]

## Remove the element with value dog
list_object.remove('dog')

## Reverse the order of a list
list_object.reverse()

## Sort a list (ascending by default)
list_object.sort()
list_object.sort(reverse=True)
```

The `sort()` method actually accepts two parameters: key and reverse. `reverse` directs the order of the sort: ascending or descending. `key` accepts a callable object which is used to sort the list:

```python
## We're going to sort the words in this sentence by size
phrase = 'the brown dog jumps over the clever fox'
words = phrase.split()
words
words.sort(key=len)
words
```
If you don't want to modify a list, you can use the following:

`sorted()`: returns a sorted copy of the list.
`reversed()`: returns an iterator object, which you can pass to the `list()` constructor to create an actual list.

These will work on any finite iterable source object.

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
We can remove items with the `del` command: `del <dictionary>[<key-name>]`.

```python
del team[2]
```

You can get the size of a list with `len(team)`.

Internally a dictionary maintains references to the key and value objects. This means two different dictionaries could reference the same key and value objects.

```python
things = [('Mikey', 12), ('Ralphy',  8), ('Kiki', 16)]
thangs = dict(things)
```

* Dictionary keys are immutable. Dictionary values are mutable.
* If you iterate over a Dictionary, you'll get it's keys.

Dictionary copying is shallow by default: `<dictionary>.copy()`. You can create a deep copy by 

```python
things = { 'name': 'Adam', 'age': 12 }

# Option-1: Shallow Copy
thangs = things.copy()

# Option-2: Deep Copy

```
* Updating an existing key, updates the key's value

* Dictionaries are iterable.
* <dictionary>.keys(): returns a list of keys from a given dictionary.
* <dictionary>.values(): returns a list of values from a given dictionary.
* <dictionary>.items(): iterates over a dictionary returning a tuple with the key and value.

You can determine if a value is or is not a key in a dictionary:

```python
<key-name> in <dictionary>
<key-name> not in <dictionary>
```

```python
things = {...}
from pprint import pprint as pp
pp.(things)
```

### Tuples

A **Tuple** is an immutable sequence of arbitrary objects: integers, floats, strings, etc. The following are ways you can initialize a tuple:

```python
## single element tuple
tup = (123, )

## empty tuple
tup = ()

tuple unpacking...
x, y = func_returning_two_tuples()

## you can convert a list to a tuple with....
tuple(<list>)
```

Tuples can be Elements of a tuple are referenced like those of a list.

```python
t = ("a", 1, 2.3)
t[0]
```

* You can concatenate two or more Tuples with the plus operator.
* You can iterate over a Tuple with a for-loop. 

You can have nested Tuples:

```python
things = ((1, 2), (3, 4))
things[0][0]
```

Tuple unpacking is a destructuring operation.

You can determine membership in a tuple with the following:

```python
1 in (1, 2, 3, 4)
5 not in (1, 2, 3, 4)
```
Python has an idiom for swapping values:

```python
a = 'jelly'
b = 'bean'

print(a, b)

a, b = b, a

print(a, b)
```

### Sets

Unordered collection of unique items.

p = {1, 2, 3, 4}

## When you init a set like this, duplicates are 
## removed
p = set([1, 2, 3, 4, 4])

type(p) == 'set'

You can determine membership in a set with the `in` and `not in` operators:

```python
p = {2, 4, 6, 8, 10}
3 in p
3 not in p
```

* You can add values to an existing set with the `add()` method: `<set>.add(<value>)`
* Adding a value that already exist does nothing.
* You can remove an item from the set with the `remove()` method: `<set>.remove()`
* You can make a shallow copy of a set with the `copy()` method.
* You can merge two sets with the `<set>.update()` method.

```python
a = {1, 3, 5}
b = {2, 4, 6}
a.update(b)
a ## shows 1, 2, 3, 4, 5, 6
```

You can execute set algebra with sets: unions, difference, and intersections. You can also evaluate whether two sets are
subset, superset, or disjointed.

<setA>.union(<setB>)
<setA>.difference(<setB>)
<setA>.intersection(<setB>)

<setA>.issubset(<setB>)
<setA>.issuperset(<setB>)
<setA>.isdisjoint(<setB>)


```python
## Returns a relational set
set([3, 2, 1, 1])
```

### Ranges

A range is a type of sequence representing an arithmetic progression of integers e.g., 1, 2, 3, 4...

```python
## Explicit starting position and increment of 1
range(<start>, <stop>)

## Default starting position of 0 and increment of 1
range(<stop>)

## Explicit starting, ending, and increment
range(<start>, <stop>, <increment>)
```

...for example...

```python
## Creates a range object from 0 to 10
range(10)

## Creates a range object from 1 to 10
range(1, 10)

## Creates a range object from 1 to 10 by 2's 1, 3, 5
range(1, 10, 2)
```

You can create a list of numbers with the pattern, which creates a list with values 0 thru 4:

```python
list(range(5))
```
Try to iterate over an object whenever you can.

If you need a count and value, use the `enumerate()` function. This function returns a tuple `(count, value)`.

```python
t = [1 , 33, 2, 32, 12]
for p in enumerate(t):
    print(p)
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

Python, like JavaScript, supports closures. A **closure** is a functions inside of another functions.

* A closure can reference variables declared in the parent function.
* A closure can be returned by the parent function

You can employ a closure whenever you want a function to reference values that might change at runtime yet remain static from one invocation to the next.

```python
def foo(name):
    whatevs = 'something'

    def bar(name):
        return ' '.join([name, whatevs])

    return bar


something = foo('kenny')

## The following prints "adam something" to the REPL
print(something('adam'))
```

### Exception Handling

Exceptions are a mechanism for interrupting normal program flow in response to an error event and continuing in a surrounding context. An exception will look something like the following:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\abomb\dev\adamfortuno\Training.Python.Concepts\exceptional.py", line 18, in convert
    numbers.append(mapping[token])
KeyError: 'sink'
```

The `KeyError` is the type of the exception thrown. `sink` is the error message. It is part of the exception's payload.

Error handling in Python is handing through a `TRY EXCEPT` statement:

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


## Catch either a key error, type error, or generic exception.
## Notice we employ the same handler for key and type errors.
try:
    last_name = teacher['a']
except (TypeError, KeyError):
    print('Error accessing student name')
except Exception:
    print("Something happened. I'm just a *@#$ that likes big @&#@.")

## Catch either a key error, type error, or generic exception.
## We're not taking any actuon when a type or key error occurs.
## We can't have an empty code block, so we use `pass` to tell
## Python to do nothing here.
try:
    last_name = teacher['a']
except (TypeError, KeyError):
    pass
except Exception:
    print("Something happened. I'm just a *@#$ that likes big @&#@.")
```

A single handler can capture multiple exceptions. You implement this by specifying the exceptions in a tuple.

```python
import sys

## Accessing the exception object
except Exception as error:
    print(f"An error occurred: {error!r}", file=sys.stderr)
```

*NOTE:* If you use the `!r` after your expression, the REPL representation will be inserted into your string. In the case of exceptions, this gives us more detail about the exception.

Raise an exception with the `raise` keyword. The following are a few examples calling raise:

```python
## Without a parameter, `raise` re-raises an existing exception:
try:
    last_name = teacher['a']
except (TypeError, KeyError):
    print("Something happened. I'm just a *@#$ that likes big @&#@.")
    raise
```

* Python provides several standard exception types.
* Invalid parameters typically generate a `ValueError`.
* You can generate a `ValueError` by passing it as a parameter to `raise`
* You can then catch and handle `ValueError` errors like any other error.

```python
#!/usr/bin/env python3

def sqrt(x):
    try:
        return_value = None

        if x < 1:
            raise ValueError('Cannot compute the square root of values less than 1.')
        
        return_value = 1
    except ValueError as err:
        print(f"Bad Stuff: {err}")
    
    return return_value

print(sqrt(1))
print(sqrt(0))
```

Exceptions are a part of a function's API as well as certain protocols.

* Sequences should raise an IndexError for out-of-bounds indexing.
* Exceptions must e implemented and documented.
* Built-in exceptions are often the right ones to use.

You can create your own exceptions.

There are two approaches to handling potentially dangerous situations:

1. "Look before you leap" promotes verification of the system's state prior to taking some action. For example, ensuring a file is present before attempting to access it.
2. "Easier to ask forgiveness than permission" promotes handling bad things that might have happened after you tried to do whatever you did. For example, just access the file. If it's not there or it's the wrong type, handle that exception.

Python embraces EAFP. Issues generate exceptions

```python
## You can introduce a `finally` block with the 
## following syntax:
try:
    ...
except:
    ...
finally:
    ...
```

There are occasions where you'll have to use platform specific code. To interact with console on Windows, you'll use the  `msvcrt` module. To interact with the console on MacOS or Linux, you'll use the `tty`, `termios`, and `sys` modules. The following module loads the correct module based on it's presence using try-catch-finally blocks:

```python
## module definition...

try:
    import msvcrt

    def getkey():
        return msvcrt.getch()

except ImportError:
    import sys, tty, termios

    def getkey():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        
        return ch
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

You can list the modules on your system with `help('modules')`.

## Virtual Environments

Python installs modules centrally. Central management can be a problematic when separate projects include different versions of the same module. A **virtual environment** isolate projects from one another providing a sandbox for each solution.

Virtual environments are implemented through the `venv` module, which ships as a standard library in Python3.

1. Create a new directory: `mkdir environments`
2. Navigate to the new directory: `cd ./environments`
3. Create a new virtual environment: `python3 -m venv foobar`. This creates a directory named `foobar`.

**NOTE:** Use of `python3 -m venv` is the preferred way to create virtual environments as of Python 3.6 and greater.

4. Load the environment's configuration script: `source foobar/bin/activate`.

At this point, you're in your environment's shell. You can exit the environment by running the command `deactivate`.

Older versions of Python used a module named `virtualenv` in place of `venv`. `virtualenv` wasn't included as a standard library pursuant, you had to install it first.

```python
## Setting up a virtual environment
pip install virtualenv

## Create the environment
mkdir ./environments && cd ./environments

## Option-1: Create an environment using the current version
## of Python
virtualenv foobar

## Option-2: Create an environment using a specific version
## of Python
virtualenv --python=<python_version> <env_name>

## Activate the environment
cd ./foobar
source ./bin/activate
```

## Expressions, Conditional Logic, and Loops

Python implements the following comparison operators:

```Python
<var> == 3                          ## Equal to
<var> != ''                         ## Not equal to
<var> == 3 and <var> != 2           ## Logical AND
<var> == 3 or <var> != 2            ## Logical OR
"adam" in team                      ## Determines if a value is in a list
not <expression>                    ## Express Not Evaluate to True
```

Python employs a traditional if, else-if, and else type conditional logic:

```python
if <expression>:
    do-something
elif <expression>:
    do-something
else:
    do-something
```

...for example...

```python
number = 2

if number == 2:
    print('Yes')
```

Language authors offer a terniary version:

```python
<true-condition> if <expression> else <false-condition>
```

...for example...

```python
'larger' if a > b else 'smaller'
```

And, you can build complex expressions with the `and` and `or` operators:

`if ( x = 1 and y = 12 )`

These work exactly like you'd expect.

Python has two types of loops:

* For: behaves like a for-each look in another languages e.g., PowerShell.
* While: behaves like While loops in Java or C++

The for loop iterates over an "iterable" (e.g., list, tuple, etc.):

```Python
## For-Each Loop
for <obj> in <list>:

t = ['adam', 'billy', 'suzie']
for each i in t:
```

Python doesn't implement the traditional `for` loop:

```javascript
for (i = 0; i < 20; i++) {
    console.log(`This is iteration ${i}`)
}
```

You can mimic the behavior using a range object. 

```python
for index in range(10):
    print(index)
```

Python implements are pretty standard `while` loop. The loop takes an expression. It continues executing until the expression is false:

```python
## While Loop
while a < 10:
    a += 1

## There is no do...while loop in Python.
## Developers use breaks to mimic that flow
while 1 == 1:
    do-something

    if done == True:
        break
```

You can break loop execution with `break`, and you can skip to the next iteration with `continue`.

```python
## Stops the loop from executing
break

## Continues the loop without running this iteration
continue
```

### Classes and Objects

Python implements the traditional OOP class to define an object:

```Python
class Door:
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
```

* By convention, class names in Python start with a capitol letter.
* Methods always take `self` as thier first parameter.
* There is no private or protected scope for data members in Python
* You define static variables in the body of the class
* You define data members in the `__init__()` method

```python
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

Protocols xxxx

* Container: 


* Sized: 
* Iterable: 
* Sequence: 
* Mutable Sequence: 
* Mutable Set: 
* Mutable Mapping: 

### File IO Access

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

You mode (w, a, etc.) determines whether what you've written with `write()` overrites your file vs. appends to it.

```python
## Overrites a file if it exists
file = open("things.txt", "w")
file.write("things")

## Appends to an existing file
file = open("things.txt", "a")
file.write("things")
```
Since you'll almost always access a file with-in a `try-except-finally` block, Python gives you a shorthand `with`:

```python
file_name = 'something.txt'

with open(file_name, mode='rt', encoding='utf-8') as source:
    return [ int( line.strip() ) for record in source ]
```

The `With` constructs closes the file connection when the block terimates.

The `With` construct works on things beside files. It will work on anything that implements the construct management protocol.

```python
from contextlib import closing

class MyClass:
    __init__():
        this.open = True


    def close():
        this.open = False


def foobar(name):
    with closing(MyClass(name)) as MyObject:
        MyObject.open()
        MyObject.use()
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

## Iterables

Comprehensions are a concise syntax for describing lists, sets, and dictionaries. The syntax for each collection's comprehension is slightly different:

* Lists: Comprehensions are enclosed in square brackets, taking the form: `[expression(item) for item in <set>]`
* Set: Comprehensions are enclosed in curly braces, taking the form: `{expression(item) for item in <set>}`
* Dictionary: Comprehensions are enclosed in curly braces, taking the form:

```
{
    key-expression(item): value-expression(item) for item in <set>
}
```

For example...

```python
## List Comprehension
words = "i love to write big long complicated sentences to wow my readers.".split()
[len(word) for word in words]

## Set Comprehension
from math import factorial
{ len(str(factorial(x))) for x in range(20) }

## Dictionary Comprehension
ctry_to_cap = {
    'United States': 'Washington',
    'United kingdom': 'London',
    'France': 'Paris',
    'Brazil': 'Brasilia'
}
{ capital: country for country, capital in ctry_to_cap.items() }
```

* In the example, we unpack the tuple returned by `ctry_to_cap.items()` in to `country` and `capital` respectively
* You can assign the result of a comprehension to a variable
* Comprehensions should have no side-effects

Comprehensions permit certain values to be filtered out.

1. Create a filtering function. Function should return False for values to be removed and True for values to be retained.
2. The function should take the form: `[item for item in <list> if <filter-function>()]`

```python
from math import sqrt

def is_prime(x):
    isPrime = True

    if x < 2:
        isPrime = False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            isPrime = False

    return isPrime

print([x for x in range(101) if is_prime(x)])
```
## Iteration Protocols

Iteration protocols involve getting items in a collection one-by-one and doing something with them. The most common method of iterating over a collection is with a `For` loop, which iterates over the whole sequence.

* Iterable Protocol: involves passing an interable-object to the `iter()` function receiving back an iterator
* Iterator Objects: iterator object can be passed to the `next()` function to get the next value in the collection

```python
p = [1, 2, 3, 4]
p_it = iter(p)
next(p_it)
```

## Generator Functions

* A generator is a function with one or more yield statements with-in it.
* Generators are lazy; computation happens just-in-time

```python
#!/usr/bin/env python3

## Creating a generator function
def foo():
    yield 1
    yield 2
    yield 3

## Calling a generator
f = foo()

print(next(f))
print(next(f))
print(next(f))

## This will generate an error as their is no further yields
print(next(f))
```

* Generator expressions are a cross between generators and comprehensions.
* Generators are single use objects.
    * To recreate a generator from a generator expression, you must execute the expression again.

```python
sum( (x * x for x in range(1, 10000001)) )
```

Iteration is a central feature of Python. Python provides a series of functions to exploit iterators, and built-in functions are expanded by the `itertools` module.

`any(<iterable>)` determines if any elements are true.
`all(<iterable>)` determines if all elements are true.
`zip()` syncronizes iteration across two iterables.
`sum()`
`min()`
`max()`


```python
sunday = [12, 14, 15, 22, 13, 22, 31]
monday = [22, 21, 19, 24, 23, 19, 41]
tuesday = [34, 22, 20, 18, 25, 27, 29]

## Combines the two series
for item in zip(sunday, monday):
        print(item)

## Get the average temp for the first sample
for sun, mon in zip(sunday, monday):
    print( "avg = ", (sun + mon) / 2 )

## Get the min, max, and avg temp for each sample
for temps in zip(sunday, monday, tuesday):
    print( f"min = {min(temps):4.1f}, max = {max(temps):4.1f}, avg = {sum(temps) / len(temps):4.1f}" )
```

* Iterable objects can be iterated item by item.
* Generators are iterators
* Generators can maintain explicit internal state between yields

## Arthmatic Operators

Addition +
Subtraction -
Division /
Exponent **
Multiplication *

## Frequently Asked Questions (FAQ)
(Q) How do I clear the session in the REPL?

Use the `system` method of the `os` module to run the `cls` command:
```Python
import os

## On windows...
os.system('CLS')

## On MacOS
os.system('clear')
```

(Q) Can I use Python with .NET Libraries?

You can use IronPython. IronPython is a port of the Python programming language to the .NET framework. The following article talks about using IronPython to script the SMO library: [Using SMO to manage a MS SQL Database](http://www.ironpython.info/index.php?title=Using_SMO_to_manage_a_MS_SQL_Database).
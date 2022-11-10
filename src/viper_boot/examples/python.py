"""Example Python Module."""


class InvalidIntegerError(RuntimeError):
    """Error generated if an invalid integer input is given."""

    pass  # pylint: disable=unnecessary-pass


def add_number(operand_one: int, operand_two: int) -> int:
    """
    Accept two integer values and sum them up and return the sum.

    Example:
        >>> add_number(5 + 5)  # xdoctest: +SKIP
        10

        >>> add_number(1 + 1)  # xdoctest: +SKIP
        2

        >>> add_number(-1 + 2)  # xdoctest: +SKIP
        InvalidIntegerError

    Parameters:
        operand_one (int): first number
        operand_two (int): second number

    Raises:
        InvalidIntegerError: If operand_one or operand_two is less than 0.

    Returns:
        Sum of two numbers
    """
    if operand_one < 0 or operand_two < 0:
        raise InvalidIntegerError(
            f"""operand_one or operand_two is less than zero:
            operand_one={operand_one}, operand_two={operand_two}"""
        )

    add: int = operand_one + operand_two
    return add

# pylint: disable=pointless-string-statement
# ==========
# Print
# ==========


"""
print(1)
    1

print((1))
    1

print(1, 2)
    1 2

print((1, 2))
    (1, 2)

# To printing on the same line use "end" parameters of the print function
# "end" takes the values which is printing at the end of the output.
print(1, end=" ")
print(2)
    1 2

print("G","F", sep="", end="")
print("G")
    GFG

print("09","12","2016", sep="-", end="\n")
    09-12-2016

print("Red","Green","Blue", sep=",", end="@")
print("hello")
    Red,Green,Blue@hello
"""

# ==========
# Swap Two Variables
# ==========

"""
x, y = y, x
"""


# ==========
# Underscore in Python
# ==========

"""
Single Underscore In Interpreter:
================================
_ returns the value of the last executed expression value
in Python Prompt/Interpreter

>>> a+b
20
>>> _
20
>>> _* 2
40


Single Underscore for ignoring values:
=====================================
# Ignore a value of specific location/index
for _ in range(10)
    print ("Test")

# Ignore a value when unpacking
a,b,_,_ = my_method(var1)


Single Underscore after a name:
==============================
Python has theirs by default keywords which we can not use as the
variable name. To avoid such conflict between python keyword and
variable we use underscore after the name

def my_definition(var1=1, class_=MyClass):
    print(var1)
    print(class_)


Single Underscore before a name:
===============================
Leading Underscore before variable/function /method name indicates to
the programmer that It is for internal use only, that can be modified
whenever the class wants. Here name prefix by an underscore is treated
as non-public.
If specify from Import * all the names starting with _ will not import.
Python does not specify truly private so this one can be called directly
from other modules if it is specified in __all__, We also call it weak Private

class Prefix:
    def __init__(self):
        self.public = 10
        self._private = 12
test = Prefix()

print(test.public)
print(test._private)
    10
    20


Single underscore in numeric literals:
=====================================
The Python syntax is utilized such that underscores can be used as visual
separators for digit grouping reasons to boost readability.
This is a typical feature of most current languages and can aid in the
readability of long literals, or literals whose value should clearly
separated into portions.

# grouping decimal for easy readability of long literals
amount = 10_000_000.0

# grouping hexadecimal for easy readability of long literals
addr = 0xCAFE_F00D

# grouping bits  for easy readability of long literals
flags = 0b_0011_1111_0100_1110


Double underscore before a name:
===============================
The leading double underscore tells the Python interpreter to rewrite the
name in order to avoid conflict in a subclass. Interpreter changes variable
name with class extension and that feature known as the Mangling.

class MyClass():
    def __init__(self):
        self.__variable = 10

>>> obj = MyClass()
>>> obj.__variable
    AttributeError: MyClass instance has no attribute "__variable"

>>> obj._MyClass__variable
10


Double underscore before and after a name:
=========================================
The name starts with __ and ends with the same considering special methods
in Python. Python provides these methods to use as the operator overloading
depending on the user. Python provides this convention to differentiate
between the user-defined function with the module’s function

class MyClass():
    def __add__(self,a,b):
        print (a*b)

>>> obj = MyClass()
>>> obj.__add__(1,2)
2
>>> obj.__add__(5,2)
10
"""


# ==========
# __name__
# ==========

"""
__name__ (A Special variable) in Python:
=======================================
Since there is no main() function in Python, when the command to run a python
program is given to the interpreter, the code that is at level 0 indentation
is to be executed. However, before doing that, it will define a few special
variables. __name__ is one such special variable. If the source file is
executed as the main program, the interpreter sets the __name__ variable to
have a value “__main__”. If this file is being imported from another module,
__name__ will be set to the module’s name.

if __name__ == "__main__":
    print ("File1 is being run directly")
else:
    print ("File1 is being imported")
"""


# ==========
# __eq__
# ==========

"""
__eq__ method in Python:
=======================
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    if isinstance(other, Person):
            return self.age == other.age

        return False

john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)
mary = Person("Mary", "Doe", 27)

print(john == jane)
    True

print(john == mary)
    False

print(john == 20)
    False
"""

# ==========
# __dict__
# ==========

"""
__dict__ is A dictionary or other mapping object used to store an
object’s (writable) attributes.

class DogClass:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def bark(self):
        if self.color == "black":
            return True
        else:
            return False


dc = DogClass("rudra","white")

print(dc.__dict__)
# Output: {"name": "rudra", "color": "white"}

DogClass.__dict__
# Output: mappingproxy({"__module__": "__main__",
    "__init__": <function __main__.DogClass.__init__(self, name, color)>,
    "bark": <function __main__.DogClass.bark(self)>,
    "__dict__": <attribute "__dict__" of "DogClass" objects>,
    "__weakref__": <attribute "__weakref__" of "DogClass" objects>,
    "__doc__": None})
"""

# ==========
# vars()
# ==========

"""
-   The vars(object) function returns the __dict__ attribute of the object
    as we know the __dict__ attribute is a dictionary containing the object"s
    changeable attributes.

-   If no value is specified for the vars() function it acts as
    pythons locals() method.

a = "Hello"
b - "World"

print(vars()["a"])
print(vars()["b"])
    Hello
    World


class MissingClass(dict):
    def __missing__(self,key):
        return "{" + key + "}"

_str = "This is {dog_name} and he has {eye_color} eyes"
dog_name, eye_color = "tiger", "black"

print(_str.format(**MissingClass(vars())))

del dog_name
print(_str.format_map(MissingClass(vars())))

del eye_color
print(_str.format_map(MissingClass(vars())))

    This is tiger and he has black eyes
    This is {dog_name} and he has black eyes
    This is {dog_name} and he has {eye_color} eyes
"""

# ==========
# Python Class Object to JSON
# ==========

"""
import json

class Laptop:
    name = "My Laptop"
    processor = "Intel Core"

# Create object
laptop1 = Laptop()
laptop1.name = "Dell Alienware"
laptop1.processor = "Intel Core i7"

#convert to JSON string
jsonStr = json.dumps(laptop1.__dict__)

# Print json string
print(jsonStr)

    {"name": "Dell Alienware", "processor": "Intel Core i7"}
"""

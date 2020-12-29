# 1. instll python & PyCharm
# 2. Keyword, can't use variable name nor function name
# False    await  else   import pass
# None break  except in raise
# True class  finally    is return
# and  continue   for    lambda try
# as   def    from   nonlocal   while
# assert   del    global not    with
# async    elif   if or yield
import keyword

print(keyword.kwlist)


# identifier a to z , A to Z, 0 to 9, cannot start with a digit eg) 1variable, cannot use keyword
# statement
# multiline a = 1 + 2 + 3 \
#              4 + 5 + 6
# multiline a = (1 + 2 + 3
#              4 + 5 + 6)

# for i in range(1,11):
#   print(i)
#   if i == 5:
#       break

# comment # multiline comment """ aaa """   docstring

def double(num):
    """function to double"""
    return 2 * num


print(double.__doc__)

# Variable
# number = 1 url="www.pycharm.com"
# a, b, c = 2, 4, "hello"
# Constant
# PI = 3.14
# GRAVITY = 9.8
# import constant
# print(constant.PI)
# Literals
# Numeric Literal
# a = 0b1010 #Binary Literals
# b = 100 #Decimal Literal
# c = 0o310 #Octal Literal
# d = 0x12c #Hexadecimal Literal

# Float Literal
# float_1 = 10.5
# float_2 = 1.5e2

# Complex Literal
x = 3.14j
print(x)

# String literal
# strings = "This is Python"
# char = "C"
# multiline_str = """This is a multiline string with more than one line code."""
# unicode = u"\u00dcnic\u00f6de"
# raw_str = r"raw \n string"

# Boolean literals
# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# Special literals
# drink = "Available"
# food = None

"""
def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)
menu(drink)
menu(food)
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set
print(fruits)
print(numbers)
print(alphabets)
print(vowels)
"""

# Data Type
"""
    #number
    a = 5
    print(a, "is of type", type(a))
    a = 2.0
    print(a, "is of type", type(a))
    a = 1+2j
    print(a, "is complex number?", isinstance(1+2j,complex))
    #List
    a = [5,10,15,20,25,30,35,40]
    # a[2] = 15
    print("a[2] = ", a[2])
    # a[0:3] = [5, 10, 15]
    print("a[0:3] = ", a[0:3])
    # a[5:] = [30, 35, 40]
    print("a[5:] = ", a[5:])
    #Tuple #Tuples are immutable. Tuples once created cannot be modified.
    t = (5,'program', 1+3j)
    # t[1] = 'program'
    print("t[1] = ", t[1])
    # t[0:3] = (5, 'program', (1+3j))
    print("t[0:3] = ", t[0:3])
    # Generates error
    # Tuples are immutable
    t[0] = 10
    #String multiline string using triple quotes,
    s = "This is a string"
    print(s)
    s = '''A multiline
    string'''
    print(s)
    #set
    a = {5,2,3,1,4}
    # printing set variable
    print("a = ", a)
    # data type of variable a
    print(type(a))
    #dictionary  {key:value}
    d = {1:'value','key':2}
    print(type(d))
    print("d[1] = ", d[1]);
    print("d['key'] = ", d['key']);
    # Generates error
    print("d[2] = ", d[2]);
    #conversion between data types
    # int(), float(), str()
    # set([1,2,3])
    # tuple({5,6,7})
    # list('hello')
"""

# type conversion ,implicit, explicit
"""
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))
--------------------------------------------
num_int = 123
num_str = "456"
print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))
print(num_int+num_str)
-------------------------------------------
explicit type conversion
<required_datatype>(expression)
num_int = 123
num_str = "456"
print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
"""

# python IO and Import
"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Here, objects is the value(s) to be printed.
The sep separator is used between the values. It defaults into a space character.
After all values are printed, end is printed. It defaults into a new line.
The file is the object where the values are printed and its default value is sys.stdout (screen). Here is an example to illustrate this.
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
#output formatting
x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
x = 12.3456789
print('The value of x is %3.2f' %x)
The value of x is 12.35
print('The value of x is %3.4f' %x)
The value of x is 12.3457
# input
num = input('Enter a number: ')
Enter a number: 10
int('2+3')
eval('2+3')
#import
import math
print(math.pi)
from math import pi
pi
"""

# Operator
"""
x = 15
y = 4
# Output: x + y = 19
print('x + y =',x+y)
# Output: x - y = 11
print('x - y =',x-y)
# Output: x * y = 60
print('x * y =',x*y)
# Output: x / y = 3.75
print('x / y =',x/y)
# Output: x // y = 3
print('x // y =',x//y)
# Output: x ** y = 50625
print('x ** y =',x**y)
Operator   Meaning    Example
>  Greater than - True if left operand is greater than the right  x > y
<  Less than - True if left operand is less than the right    x < y
== Equal to - True if both operands are equal x == y
!= Not equal to - True if operands are not equal  x != y
>= Greater than or equal to - True if left operand is greater than or equal to the right  x >= y
<= Less than or equal to - True if left operand is less than or equal to the right    x <= y
x = 10
y = 12
# Output: x > y is False
print('x > y is',x>y)
# Output: x < y is True
print('x < y is',x<y)
# Output: x == y is False
print('x == y is',x==y)
# Output: x != y is True
print('x != y is',x!=y)
# Output: x >= y is False
print('x >= y is',x>=y)
# Output: x <= y is True
print('x <= y is',x<=y)
Operator   Meaning    Example
and    True if both the operands are true x and y
or True if either of the operands is true x or y
not    True if operand is false (complements the operand) not x
x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)
#bitwise operators
Operator   Meaning    Example
&  Bitwise AND    x & y = 0 (0000 0000)
|  Bitwise OR x | y = 14 (0000 1110)
~  Bitwise NOT    ~x = -11 (1111 0101)
^  Bitwise XOR    x ^ y = 14 (0000 1110)
>> Bitwise right shift    x >> 2 = 2 (0000 0010)
<< Bitwise left shift x << 2 = 40 (0010 1000)
#Assignment operators
Operator   Example    Equivalent to
=  x = 5  x = 5
+= x += 5 x = x + 5
-= x -= 5 x = x - 5
*= x *= 5 x = x * 5
/= x /= 5 x = x / 5
%= x %= 5 x = x % 5
//=    x //= 5    x = x // 5
**=    x **= 5    x = x ** 5
&= x &= 5 x = x & 5
|= x |= 5 x = x | 5
^= x ^= 5 x = x ^ 5
>>=    x >>= 5    x = x >> 5
<<=    x <<= 5    x = x << 5
# identity operators
Operator   Meaning    Example
is        True if the operands are identical (refer to the same object)   x is True
is not    True if the operands are not identical (do not refer to the same object)    x is not True
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)
#membership operators
Operator   Meaning    Example
in         True if value/variable is found in the sequence    5 in x
not in     True if value/variable is not found in the sequence    5 not in x
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)
"""

# python namespace and scope
"""
a = 2, 2 is an object stored in memory and a is the name we associate it with.
We can get the address (in RAM) of some object through the built-in function id().
a = 2
print('id(2) =', id(2))
print('id(a) =', id(a))
def printHello():
    print("Hello")
a = printHello
a()
Example of Scope and Namespace in Python
def outer_function():
    b = 20
    def inner_func():
        c = 30
a = 10
def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =', a)
    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
---------------------------------------------------
def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)
    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
def outer_function():
    a = 20
    print('outer')
    def inner_function():
        a = 30
        print('inner')
        print('a =', a)
    inner_function()
    print('inner')
    print('a =', a)
a = 10
outer_function()
print('a =', a)
"""

# If else statement
"""
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
"""
# for loop
"""
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# variable to store the sum
sum = 0
# iterate over the list
for val in numbers:
	sum = sum+val
print("The sum is", sum)
---------------------------
range() function
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))
genre = ['pop', 'rock', 'jazz']
# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])


digits = [0, 1, 5]
# for loop with else... if for loop is exhausted, then else part is executed.
for i in digits:
    print(i)
else:
    print("No items left.")
----------------------------------------------------------    
# program to display student's marks from record
student_name = 'Soyuj'
marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')
"""
# break , continue statement
"""
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")
for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")
#pass
will implement later
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

def function(args):
    pass
"""
# Function
"""
function definition : 
def function_name(parameters):
	statement(s)


def greet(name):
    print("Hello, " + name + ". Good morning!")
greet('Paul')
print(greet.__doc__)
Scope and lifetime
def my_func():
	x = 10
	print("Value inside function:",x)
x = 20
my_func()
print("Value outside function:",x)
"""

j = 2
vari = complex(4 + 14 * j)
print(vari)
a, b = 2, 3
print(a, b)

string = "this is test"

list_a = [a, b, vari, string]

print(list_a)

tup = (a, b, string)

print(tup)

A = {0, 0, 0, 0, 0, 0}
# print(A)
A = set('PYTHON')
# B = set('1,2,3')
print(A)
# print(B)

# dictionary
user = {'name': 'jun', 'age': '10', 'sex': 'male'}

print(user['age'])

print(user.get('name'))
print(user.items())
print(user.keys())
print(user.values())
print(user.copy())
print(user.clear())

string = "This year is "
date = 2020
date = str(date)

final = string + date
print(final)

lunch = ["hot dog", "hamburg", "donut"]
snack = ["chip", "fry", "eggs"]

lunch.extend(snack)

print(lunch)

print(2 ** 4, 5 / 2, 5 // 2)  # ** exponential, / divide // integer divide

age = 5  # input("what is your age:")

if (int(age) > 100):
    print("You probably lie")
else:
    print("You are telling truth")

if (int(age) > 100):
    print("Lie")
elif (int(age) < 50):
    print("Young")
else:
    print("old")

try:
    age = int(age)
except:
    print(age)
finally:
    print("telling the truth")

x = 0
for x in range(5, 20, 5):
    print(x)
print("End")

# List
sports = ['soccer', 'baseball', 'tennis', 'polo']

for x in sports:
    print(x)
print("End")

for x in range(len(sports)):
    print(x)
print("End")

# tuples
foods = ("pizza", "hot dog", "sushi")
x = 0
for food in range(len(foods)):
    print("The x value is: " + str(x))
    print("The food value is: " + str(food))
    print("The foods item is: " + foods[food])
    x += 1
print("End")

# dictionary
clothes = {"shirt": "red", "shoes": "black", "pant": "blue"}
for key in clothes:
    print(key)
clothe = "shoes"  # input("Choose one of them: ")
if (clothe in clothes):
    print("Your clothe is " + clothe + "of color " + clothes[clothe])
else:
    print("Error")

print(clothes["pant"])

#########Array #########
# importing array module
import array as arr

# creating a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Intial Array: ")
for i in (a):
    print(i, end=" ")

# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)

# While
cycles = 5  # input("Put the number of cycles here: ")
count = 0
while (count < int(cycles)):
    count += 1
    print("Cycle number " + str(count))
print("END")

import time

x = 1
while (True):
    print(x)
    x += 1
    time.sleep(1)
    if x == 2:
        break

cycles = 11  # input("Please put the number of cycles: ")
count = 1
while (count - 1 < int(cycles)):
    a = count
    count += 1
    if (a % 5 == 0):
        print("Error, continue")
        continue
    else:
        print("Not is multiple of 5")
    print(a)
print("End")

## pass statement is do nothing

cycles = 11  # input("Please put the number of cycles: ")
count = 1
while (count - 1 < int(cycles)):
    a = count
    count += 1
    if (a % 5 == 0):
        print("Error, continue")
        pass
    else:
        print("Not is multiple of 5")
    print(a)
print("End")

#### Function #####
a = [1, 2, 3, 4, 5]
b = [1, 0, 1, 0, 1]
num = "5 6 7 8 9"
c = num.split()
print(c)
e = []
for x in c:
    d = int(x)
    e.append(d)
c = e
d = []
for x in range(len(a)):
    e = a[x] + b[x] + c[x]
    d.append(e)
e = min(d)
f = max(d)
g = sum(d)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


##### Define own function ######
#### Argument by name#####
def funct(a, b):
    return a + b


c = funct(b=5, a=3)
print(c)


##### Argument by position ####
def hello(name, color):
    print("Hello " + name + " your favorite color is " + color)


a = "Jun"  # input("what is your name? ")
b = "Yellow"  # input("what is your favorite color? ")
hello(a, b)


### Calling without Argument ###
def hello():
    print("hello")


hello()

#### lambda function #####
## function_name = lambda parameter: function detail #####
sum = lambda x, y: x + y
a = sum(3, 10)
print(a)


### filter function ###
## return value = filter(defined function, parameter) ###
def pair(n):
    if (n > 0 and n % 2 == 0):
        return True
    else:
        return False


numbers = []
for x in range(25):
    numbers.append(x)

pairs = filter(pair, numbers)

for x in pairs:
    print("The number " + str(x) + " is pair")


### map function ###
def sum(a, b):
    return a + b


list1 = [1, 0, 1, 0, 1]
list2 = [0, 2, 0, 2, 0]

c = map(sum, list1, list2)
print(list(c))

string1 = ["hello", "are "]
string2 = [" how", "you"]

c = map(sum, string1, string2)
print(list(c))


##### OOP #####
class house():
    def __init__(self, color, doors, kitchen, bathroom, levels):
        self.color = color
        self.doors = doors
        self.kitchen = kitchen
        self.bathroom = bathroom
        self.levels = levels

    def open(self):
        print("The door is open")

    def paint(self, c):
        self.color = c


house1 = house("blue", 5, True, 2, 1)
print(house1.color)
house1.paint("black")
print(house1.color)
house1.open()


##### Inheritance #######
class apartment(house):
    def __init__(self, color, doors, kitchen, bathroom, levels, stairs, elevator):
        house.__init__(self, color, doors, kitchen, bathroom, levels)
        self.stairs = stairs
        self.elevator = elevator

    def elevatoron(self):
        if (self.elevator == True):
            print("The elevator is in PB")
        else:
            print("You don't have elevator")


apartment1 = apartment("orange", 2, True, 2, 1, True, True)
apartment1.elevatoron()
apartment1.open()

###### File Handling #####
function = open("file.txt", "w")


# function.write()
# function.close()

def fun(x: int) -> float:
    return x * x


a = fun(4)
print(a)

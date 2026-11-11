# FUNCTIONS
# Functions are reusable pieces of code that run when you call them. Python provides built-in functions, including print().

# name = input('What is your name? ')
# print('Hello, ' + name + '!')

# On the other hand, int() converts a number, a boolean, or a string representing an integer into an integer:

print(int('5'))  # prints 5
print(int(5.0))  # prints 5
print(int(True))  # prints 1
print(int(False))  # prints 0

# Defining and Calling Functions

# You can also write your own custom functions. To do that, you use the def keyword, followed by the name you want to give your function, a pair of parentheses, and a colon. Then on a new line, you write the code your function should run. The code the function runs is also referred to as the function's body.

def hi():
    print('Hello!')

hi()

# Using Parameters and Arguments

def sum(a, b):
    print(a + b)

sum(5, 10)  # prints 15

# Returning Values From Functions
def mult(a, b):
    return a * b

print(mult(5, 10))  # prints 50

# Scope in Python 
# Scope determines where you can use a variable in your code.

# Python has additional scope rules. For now, focus on local and global scope.

# A variable created outside a function has global scope. You can use it both inside and outside functions.

# A variable created inside a function has local scope. You can only use it inside that function. Function parameters are local variables too.

tax_rate = .1

def calc_tax(price):
    tax = price * tax_rate
    return tax

print(calc_tax(100))  # prints 10.0
print(tax_rate)  # prints 0.1
print(tax) # NameError: name 'tax' is not defined


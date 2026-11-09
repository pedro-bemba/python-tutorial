name = 'Pedro Bemba' # string
age = 21 # integer

# Following Name Conventions
# First, variable names should be in lowercase, with words separated by an underscore. This is called snake case

my_variable_name = 'freeCodeCamp'
user_age = 21

# Finding the type of a variable
developer_name = 'Pedro Bemba'
print(type(developer_name)) # <class 'str'>

# There will be times in your program when you need to verify that a particular variable is a specific type before performing operations on it. This is where the isinstance() function comes in handy.

account_balance = "2000"
# If you try to perform mathematical operations like division using the account_balance variable, then you will receive an error message.

account_balance / 2

# Traceback (most recent call last):
#   File "/home/bemba/Documents/python-tutorial/declaring-variables.py", line 19, in <module>
#     account_balance / 2
#     ~~~~~~~~~~~~~~~~^~~
# TypeError: unsupported operand type(s) for /: 'str' and 'int'


# To see if account_balance is an integer, you can check using the isinstance() function like this
isinstance(account_balance, int) # False

# The isinstance() function also allows you to check for multiple types at once.
weight = 70.5
isinstance(weight, (int, float)) # True

# Conditional Statements and Comparison Operators Work

# Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.

# Comparison operators are operators that let you compare two or more values, and return a boolean value.

# ==	Equal	Checks if two values are equa
# !=	Not equal	Checks if two values are not equal
# >	Greater than	Checks if the value on the left is greater than the value on the right
# <	Less than	Checks if the value on the left is less than the value on the right
# >=	Greater than or equal	Checks if the value on the left is greater than or equal to the value on the right
# <=	Less than or equal	Checks if the value on the left is less than or equal to the value on the right

print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)

# Using if Statements
# These operators can be used in conditionals to compare values and run certain code based on whether the conditional evaluates to True or False.

# if condition:
    # pass # Code to execute if condition is True

age = 18
if age >= 18:
    print("You are an adult.")

age = 14
if age >= 18:
    print("You are an adult.") # Not printed because the condition is False

# Adding an else Clause
# But what if you also want to print something if age is less than 18? That's where the else clause comes in. The else clause runs when the if condition is false. Here's the syntax for an if...else statement:

# if condition:
    # pass # Code to execute if condition is True
# else:
    # pass # Code to execute if condition is False

age = 14
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.") # Output: You are a minor.

# Adding elif Clauses
# There might be situations in which you want to account for multiple conditions. To do that, Python lets you extend your if statement with the elif (else if) keyword.

# if condition1:
    # pass # Code to execute if condition1 is True
# elif condition2:
    # pass # Code to execute if condition1 is False and condition2 is True
# else:
    # pass # Code to execute if all conditions are False

age = 4

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:   
    print("You are a child.") # Output: You are a child.
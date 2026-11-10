# Truthy and Falsy Values, and How Do Boolean Operators and Short-Circuiting Work

# While those are very powerful, you will often run into situations where you need to compare multiple values at once. This can lead to nested conditional statements

is_citizen = True
age = 20
if is_citizen:
    if age >= 18:
        print("You are elible to vote.")
    else:   
        print("You are not elible to vote.")
else:
    print("You are not elible to vote.")

# Truthy and Falsy Values

# If you want to check whether a value is truthy or falsy, you can use the built-in bool() function. It explicitly converts a value to its boolean equivalent and returns True for truthy values and False for falsy values. 

print(bool(False))
print(bool(0))
print(bool(""))

print(bool(True))
print(bool(1))
print(bool("Hello"))

# Boolean Operators
# There are three Boolean operators in Python: and, or, and not.

is_citizen = True
age = 20

print(is_citizen and age) # Output: True

if is_citizen and age >= 18:
    print('You are elible to vote.') # Output: You are elible to vote.
else:
    print('You are not elible to vote.')

age = 19
is_employee = False

print(age or is_employee) # Output: True

is_student = True

if age < 18 or is_student:
    print('You are elible for a student discount.') # Output: You are elible for a student discount.
else:
    print('You are not elible for a student discount.')

print(not "")
print(not "hello")
print(not 0)
print(not 1)
print(not False)
print(not True)

is_admin =  False

if not is_admin:
    print('Access denied non-administrator')
else:
    print('Welcome, administrator!')
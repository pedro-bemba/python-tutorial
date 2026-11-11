# Identity Operators 
# In Python, variables are names that refer to objects. Identity operators check whether two operands refer to the same object. The is operator returns True if they do, and False otherwise. The is not operator returns the opposite result.

# Checking for None
# You can use is None to check whether a value is missing, or is not None to check whether it is present:

response = None

print(response is None)
print(response is not None)

response = False

if response is None:
    print('No answer yet.')
else:
    print('An answer was given.')
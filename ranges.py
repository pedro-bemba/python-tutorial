# The range() function is used to generate a sequence of integers. Here is the basic syntax for the range() function:

# range(start, stop, step)

for num in range(3):
    print(num)

# If a start argument is not specified, then the default is 0. Otherwise, you can use the optional start argument to start the sequence of integers at an integer other than 0. Here is an example of generating a sequence of integers between 1 and 4:
for num in range(1, 5):
    print(num)

# By default the sequence of integers will increment by 1. But if you want to change that default, then you can use the optional step argument. Here is an example of generating a sequence of even integers between 2 and 10:
for num in range(2, 11, 2):
    print(num)

# If you want to generate a sequence of integers in decrementing order, then you can use a negative integer for the step argument, like this:
for num in range(40, 1, -10):
    print(num)

# To generate a list of integers, pass a range to the list() constructor. The list() constructor converts an iterable into a list. Here is an example of generating a list of even integers between 2 and 10:
num = list(range(2, 11, 2))
print(num)
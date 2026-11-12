# A tuple is a Python data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types like this:
dev = ('Pedro', 21, 'Python Dev')

# The commas create the tuple, so parentheses are optional in an assignment like this:
dev1 = 'Bemba', 21, 'NodeJS'

# To create a tuple with one element, you need a trailing comma:
single_value = (4,)

not_a_tuple = (5)
# An empty tuple is written as ().

# Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created.

# Accessing Tuple Elements
# To access an element from a tuple, you can use bracket notation and the index number:
print(dev[0])

# Using the tuple() Constructor
# Another way to create a tuple is by using the tuple() constructor like this:
developer = 'Pedro'
print(tuple(developer))

# Checking If an Element Is in a Tuple
# To check if an item is in a tuple, you can use the in keyword like this:
num = [1, 2, 3, 4]
print(1 in num)

# Unpacking Values from a Tuple
# You can also unpack items from a tuple just like you did with lists:
user = 'pedro-bemba', '1234Luanda'
username, password = user
print(username)
print(password)

# If you need to collect any remaining elements from a tuple, you can use the asterisk (*) operator like this:
user = 'pedro-bemba', 'pedro@gmail.com', '1234Luanda'
username, *credentials = user
print(username)
print(credentials)

# Using Tuples in Simultaneous Assignment
# You can create a tuple on the right side of an assignment and unpack it into the variables on the left:
first, last = 'Pedro', 'Bemba'
print(first)
print(last)

# Returning a Tuple from a Function
# A function can return a tuple by placing comma-separated values after return:
def get_coordinates():
    lat = 10
    lon = 20
    return lat, lon

coordinates = get_coordinates()
print(coordinates)

# You can unpack the returned tuple directly into variables:
x, y = get_coordinates()
print(x)
print(y)

# Slicing Tuples
# Just like with a list, you can use the slice operator on a tuple to extract a portion of it. Here is an example of extracting the items 'pie' and 'cookies' into a separate tuple:
desserts = 'ice cream', 'cake', 'pie', 'cookies'
print(desserts[1:])

# Comparing Tuples
# Python compares tuples lexicographically. This means it compares corresponding elements from left to right. The first unequal pair determines the result:
print((1, 3) < (1, 5))
# Both tuples start with 1, so Python compares 3 with 5 to determine the result.

# If all corresponding elements are equal, the shorter tuple is smaller. Tuples with the same length and equal corresponding elements are equal:
print((1 ,2) > (1, 2, 3))
print((1 ,2) == (1, 2))

# print((1, 3) < (1, 'five'))
# TypeError: '<' not supported between instances of 'int' and 'str'
# Here, the first elements are equal, but Python cannot order the integer 3 and the string 'five'.

# Later elements do not need to be comparable if an earlier pair already determines the result:
print((1, 3) < (2, 'five')) # True

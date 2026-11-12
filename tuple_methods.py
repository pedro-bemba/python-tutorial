# The count() Method
# The first method we will cover is count(). This method is used to determine how many times an item appears in a tuple. Here is an example of checking how many times the string Python appears in a tuple named programming_languages:

programming_languages = ('Python', 'Java', 'C', 'Rust', 'Python', 'C++')
print(programming_languages.count('Python'))

# The index() Method
# The next method we will look at is the index() method. This method is used to find the index where a particular item is present in a tuple. Here is an example of using the index() method to find the index for the string Java:
print(programming_languages.index('Java'))

# In this example, we are specifying where to start searching for the string Python. By passing in the number 3 as the second argument to the index() method, we are specifying to start searching at index 3. Since Python appears twice in the tuple, the index() method will return index 5 instead of index 2 because of the use of the optional start index argument.
print(programming_languages.index('Python', 3))

# You can also pass in an optional stop index. Here is a modified example of specifying a start and stop index:
print(programming_languages.index('C', 1, 5))

# The sorted() Function
# Another function commonly used with tuples is the sorted() function. In a previous lesson you learned about the sort() method for lists. Well, the sorted() function can be used on any iterable including tuples.

# Here is an example of creating a new list of numbers using the sorted() function:
num = 1, 3, 5, 1, 4
print(sorted(num))

# If you need to customize the sorting behavior for an iterable, you can use the optional reverse and key arguments. Here is an example of using the key argument to sort items in a tuple by length:
print(sorted(programming_languages, key=len))

# If you want to create a new list of values sorted in descending order, then you can use the reverse argument like this:
print(sorted(programming_languages, reverse=True))
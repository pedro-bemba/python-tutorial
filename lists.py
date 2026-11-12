# The list data type is an ordered sequence of elements that can be comprised of strings, numbers, or even other lists. Lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero.

citties = ['Los Angeles', 'New York', 'London']
citties[0] # First city
citties[-1] # Last one

# Using the list() Constructor
# Another way to create a list is to use the list() constructor. The list() constructor is used to convert an iterable into a list like this:

developer = 'Bemba'
print(list(developer))

# Getting the Length of a List
# To get the total number of elements in a list, you can use the len() function like this:
print(len(developer))

# Updating List Elements
# If you wanted to update a value at a particular index, you can do something like this:
progamming_languages = ['Python', 'Java', 'C/C++', 'Ruby']
progamming_languages[1] = 'JavaScript'
print(progamming_languages)

# Removing Elements from a List
# If you want to remove an element from a list you can use the del keyword like this:
del progamming_languages[1]
print(progamming_languages)

# Checking If an Element Is in a List
# Sometimes it is helpful to check if an element is inside the list. To do that, you can use the in keyword like this:
print('Ruby' in progamming_languages)

# Working with Nested Lists
# Sometimes it is common to have lists nested inside of other lists like this:
foods = ['rice', 'bean', ['mango', 'banana', 'orange']]
print(foods[2])
print(foods[2][1])

# Unpacking Values from a List
# Another common technique used with lists is unpacking values.

# Unpacking values from a list is a technique used to assign values from a list to new variables. Here is an example of unpacking a developer list into new variables called name, age, and job.

developer = ['Pedro', 21, 'Python Developer']
name, age, job = developer
print(name)
print(age)
print(job)

# Slicing Lists
# The last concept we will look at is the slice operator (:). Similar to strings, you can access portions of a list by using the slice operator like this:
fruits = ['mango', 'banana', 'pineable', 'tomato']
print(fruits[:1])

# In this example, the start index is 1 since that points to the second item in the list. Then we use the slice operator followed by an end index of 4, which includes everything up to (but not including), the item at that index.

# Another thing you can do with the slice operator : is specify a step interval which determines how much to increment between the indices. Let's say you had a list of numbers like this:

nums = [1,2,3,4,5,6,7]
print(nums[4::1])

# The first even number is at index 1, so that will be the start index. Since we want to go through the end of the list, then we omit the end index. Lastly, we specify 2 for the optional step interval so it will only increment by 2 instead of the default 1.


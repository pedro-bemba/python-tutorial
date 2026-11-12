# Adding Elements with append()
# The first method we will look at is the append() method. This is used to add an item to the end of the list. Here is an example of using the append() method to add the number 6 to a list of numbers:

num = [1, 2, 3, 4, 5]
num.append(6)
print(num)

# If you want to add one list at the end of another, you can also use the append() method like this:
new_num = [7, 8, 9]
num.append(new_num)
print(num)

# Adding Multiple Elements with extend()
# The extend() method is similar to the append() method, but with extend() you can add multiple elements from one list to another. Here's an example of adding the numbers 6, 8, and 10 from one list to the end of the numbers list:
old_num = [0.1, 0.2, 0.3]
new_num.extend(old_num)
print(new_num)

# Inserting Elements at a Specific Index
# To insert an element at a specific index in a list, you can use the insert() method. This method accepts two arguments: the index where you wish to insert the new item and the item you want to insert.
foods = ['orange', 'mango', 'pineaple']
foods.insert(0, 'limon')
print(foods)

# Removing Elements from a List
# If you want to remove an element from a list, you can use the remove() method. The remove() method takes the value of the element to remove as an argument:
foods.remove('limon')
print(foods)

# To remove an element at a specific index in the list, you can use the pop() method like this:
foods.pop(0)
print(foods)

# If you don't specify an index for the pop method, then the last element is removed.
foods.pop()
print(foods)

# Clearing a List
# If you need to empty the list, then you can use the clear() method like this:
foods.clear()
print(foods)

# Sorting a List
# The next method we will take a look at is the sort() method. This method is used to sort the elements in place. Here is an example of sorting a random list of numbers in place:
new_num.sort()
print(new_num)

# In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list. For example:
num = [1 ,52 ,4 ,6 ,3]
new_num = sorted(num)
print(new_num)

# Reversing a List
# The next method we will take a look at is the reverse() method. This method will reverse a list of elements in place like this:
num.reverse()
print(num)

# Finding the Index of an Element
# The last method we will take a look at is the index method. This is used to find the first index where an element can be found in a list. Here is an example of using the index method to find the language 'Java' in a programming_languages list:
animal = ['giraffe', 'bat', 'dog', 'cat']
print(animal.index('dog'))

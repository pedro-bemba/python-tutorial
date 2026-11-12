# Loops are used to repeat a block of code. In this lesson, you will learn how to work with different types of loops in Python.

programming_languages = ['Rust', 'Python', 'C', 'Java']
for language in programming_languages:
    print(language)


# Looping through Other Iterables
# You can also use a for loop to iterate through other iterables like a string. Here is an example of using a for loop to loop through the string code and print out each character:
for char in 'code':
    print(char)

# Nesting for Loops
# You can nest for loops in Python. Here is an example of a nested for loop:

categories = ['Fruit', 'Vegetables']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
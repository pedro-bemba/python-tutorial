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

# Using break and continue
# Python supports the break and continue statements.

# The break statement is used to stop the execution of a loop. Here is an example of using the break statement for a list of developer_names:

devs = ['Jess', 'Naomi', 'Tom']
for dev in devs:
    if dev == 'Naomi':
        break
    print(dev)

# The continue statement is used to skip the current iteration of a loop and move onto the next iteration. Let's modify the example from earlier to use the continue statement instead of break:
devs = ['Jess', 'Naomi', 'Tom']
for dev in devs:
    if dev == 'Naomi':
        continue
    print(dev)

# Adding an else Clause to a Loop
# Both for and while loops can be combined with an else clause, which is executed only when the loop is not terminated by a break statement. Here is an example of using multiple for loops:

words = ['key', 'apple', 'rhythm', 'fly', 'orange']
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'"{word}" contains the vowel "{letter}"')
            break

    else:
        print(f'"{word}" has no vowels')
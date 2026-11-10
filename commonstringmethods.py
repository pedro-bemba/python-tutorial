# Some Common String Methods

# upper(): Returns a new string with all characters converted to uppercase.

msg = ' Hi, Im learning python with FreeCodeCamp!'
upper_msg = msg.upper()
print(upper_msg)  # HI, IM LEARNING PYTHON WITH FREECODECAMP

# lower(): Returns a new string with all characters converted to lowercase.

lower_msg = msg.lower()
print(lower_msg)  # hi, im learning python with freecodecamp!

# strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.

stripped_msg = msg.strip()
print(stripped_msg)  # Hi, Im learning python with FreeCodeCamp!

# replace(old, new): Returns a new string with all occurrences of old replaced by new.

new_msg = msg.replace('python', 'Machine Learning')
print(new_msg)  #  Hi, Im learning Machine Learning with FreeCodeCamp!

# split(separator): Splits a string on a specified separator into a list of strings. A list groups values between square brackets. If no separator is specified, split() splits on whitespace.

split_msg = msg.split()
print(split_msg)  # ['Hi,', 'Im', 'learning', 'python', 'with', 'FreeCodeCamp!']

# join(): Joins the strings in a collection into a single string with a separator.

todo_list = ['Learn', 'Python', 'with', 'FreeCodeCamp']
joined_todo_list = ' '.join(todo_list)
print(joined_todo_list)  # Learn Python with FreeCodeCamp

# startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

starts_with_hi = msg.startswith('Hi')
print(starts_with_hi)  # False

# endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
ends_with_exclamation = msg.endswith('!')
print(ends_with_exclamation)  # True

# count(substring): Returns the number of non-overlapping occurrences of a substring in a string.
counts_o = msg.count('o')
print(counts_o)  # 2

# capitalize(): Returns a new string with the first character capitalized and the other characters lowercased
msg = 'hello, world!'
cap_msg = msg.capitalize()
print(cap_msg)

# isupper(): Returns True if the string contains at least one cased character and all cased characters are uppercase. Otherwise, it returns False

is_upper = upper_msg.isupper()
print(is_upper)

# islower(): Returns True if the string contains at least one cased character and all cased characters are lowercase. Otherwise, it returns False.

is_lower = lower_msg.islower()
print(is_lower)

# Returns a new string with the first letter of each word capitalized and the remaining letters lowercased.
title_msg = msg.title()
print(title_msg)  # Hello, World!
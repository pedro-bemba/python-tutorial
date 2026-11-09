# A string is a sequence of characters surrounded by either single or double quotation marks.

h1 = 'hello'
h2 = "hello"

# If you need a multiline string, you can use triple double quotes or triple single quotes:

h3 = """Hello,
world!"""
h4 = '''Hello,
world!'''

# If you need a multiline string, you can use triple double quotes or triple single quotes:

# Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:
msg = "It's a beautiful day!"
greeting = 'He said, "Hello!"'

# Escape the single or double quotation mark in the string with a backslash (\). With this method, you can use either single or double quotation marks to wrap the string itsel
msg = 'It\'s a beautiful day!'
greeting = "He said, \"Hello!\""

# Sometimes, you may need to check if a string contains one or more characters. For that, Python provides the in operator, which returns a boolean that specifies whether the character or characters exist in the string or not.

msg = "Hello, world!"
print("Hello" in msg)  # True
print('hey' in msg)  # False
print('Pedro' not in msg)  # True

# Now, let's look at how you can get the length of a string and work with the individual characters in a string, a process called indexing. To get the length of a string, you can use the built-in len() function

print(len(msg))  # 13

# Each character in a string has a position called an index. The index is zero-based, meaning that the index of the first character of a string is 0, the index of the second character is 1, and so on. To access a character by its index, you use square brackets ([]) with the index of the character you want to access inside.

print(msg[0])  # H

# Negative indexing is also allowed, so you can get the last character of any string with -1, the second-to-last character with -2, and so on
print(msg[-2])  # !

# Strings are immutable in Python, but you can still reassign a variable to a different string

greeting = 'hi'
greeting = 'hello'
print(greeting)

# But direct modification of a string isn't allowed
grt1 = 'hi'
# grt1[0] = 'H'  # This will raise an error


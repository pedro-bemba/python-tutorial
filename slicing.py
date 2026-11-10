# String Slicing and How Does It Work?
msg = 'Hello, guys!'

print(msg[0])
print(msg[-1])

# String slicing lets you extract a portion of a string or work with only a specific part of it

# string[start:stop]

print(msg[1:4]) # ell

# You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively. For example, here's what happens if you omit the start index

print(msg[1:])
print(msg[:4])
print(msg[:])

# string[start:stop:step]

# Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.

print(msg[0:2:4])

# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank

print(msg[::-1])
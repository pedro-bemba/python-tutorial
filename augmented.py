# Augmented Assignments Work

# Augmented assignment applies an operation to a variable and stores the result back in the same variable, all in one step.

num = 10
num += 5  # Equivalent to num = num + 5
print(num)  # Output: 15

# Arithmetic and bitwise operators have augmented assignment forms. We've looked at the addition assignment operator (+=), so let's look at others.

# The subtraction assignment operator (-=) subtracts the right operand from the left variable and stores the difference in the left variable

num -= 3  # Equivalent to num = num - 3
print(num)  # Output: 12

# The multiplication assignment operator (*=) multiplies the left variable by the right operand and stores the product back in the left variable

num *= 2  # Equivalent to num = num * 2
print(num)  # Output: 24

# The division assignment operator (/=) divides the left variable by the right and stores the result back in the left variable

num /= 4  # Equivalent to num = num / 4
print(num)  # Output: 6.0

# The floor division assignment operator (//=) floor‑divides the left variable by the right and stores the result back in the left variable

num = 6
num //= 2  # Equivalent to num = num // 2
print(num)  # Output: 3 

# The modulo assignment operator (%=) computes the remainder of the left variable divided by the right and stores it back in the left variable

num %= 2  # Equivalent to num = num % 2
print(num)  # Output: 1

# The exponentiation assignment operator (**=) raises the left variable to the power of the right and stores the result back in the left variable

power = 2
power **= 3  # Equivalent to power = power ** 3
print(power)  # Output: 8

# You can use some augmented assignment operators with strings, too. For example, the addition assignment operator makes it easy to concatenate strings

greet = 'hello'
greet += ' world' 
print(greet)  # Output: hello world

# And the multiplication assignment operator can be used to repeat a string

greet = 'ha'
greet *= 3
print(greet)  # Output: hahaha

# The subtraction and division assignment operators raise a TypeError when used with strings

greet = 'Hello'
greet -= ' World' # TypeError: unsupported operand type(s) for -=: 'str' and 'str'

greet = 'Hello'
greet /= 'World' # TypeError: unsupported operand type(s) for /=: 'str' and 'str'


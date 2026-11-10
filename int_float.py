# Work With Integers and Floating Point Numbers

# Integers and floats are the primary numeric data types in Python. With them, you can store numeric data and perform mathematical operations.

my_int1 = 4
my_int2 = -2

print(type(my_int1))
print(type(my_int2))

sum_ints = my_int1 + my_int2
subs_ints = my_int1 - my_int2
mult_ints = my_int1 * my_int2
div_ints = my_int1 / my_int2

print(f'Sum of integers: {sum_ints}')
print(f'Subtraction of integers: {subs_ints}')
print(f'Multiplication of integers: {mult_ints}')
print(f'Division of integers: {div_ints}')

# Working with Floats

my_float1 = 3.14
my_float2 = -0.5

print(type(my_float1))
print(type(my_float2))

sum_floats = my_float1 + my_float2
subs_floats = my_float1 - my_float2
mult_floats = my_float1 * my_float2
div_floats = my_float1 / my_float2

print(f'Sum of floats: {sum_floats}')
print(f'Subtraction of floats: {subs_floats}')
print(f'Multiplication of floats: {mult_floats}')
print(f'Division of floats: {div_floats}')

# This is true for other basic arithmetic operations, too, like subtraction, multiplication, and division. If you mix integers and floats, Python will return a float as the result.
sum_mixed = my_int1 + my_float1
print(sum_mixed)
print(type(sum_mixed))  # This will be a float

# Performing Complex Arithmetic Operations

# You can also perform more complex arithmetic calculations such as getting the remainder of two numbers with the modulo operator, floor division, and exponentiation with both integers and floats.

mod_ints = my_int1 % my_int2
mod_floats = my_float1 % my_float2

print(f'Modulo of integers: {mod_ints}')
print(f'Modulo of floats: {mod_floats}')

# Exponentiation raises a number to the power of another, and is done with the double asterisk operator (**)

exp_ints = my_int1 ** my_int2
exp_floats = my_float1 ** my_float2

print(f'Exponentiation of integers: {exp_ints}')
print(f'Exponentiation of floats: {exp_floats}')

# Floating Point Representation and Rounding Errors

# Sometimes, you might notice that the result of an operation involving floats has more decimal digits than expected. For example, the sum 0.1 + 0.2 equals 0.30000000000000004 instead of 0.3.

num1 = 10
num2 = float(num1)
print(num2, type(num2))

num1 = 10.0
num2 = int(num1)
print(num2, type(num2))

str_int = '10'
str_float = '10.5'

converted_int = int(str_int)
converted_float = float(str_float)

print(converted_int, type(converted_int))
print(converted_float, type(converted_float))

#  Functions for Working with Integers and Floats

# round(): Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer, and returns a whole number with no decimal places

num = 3.14159
rounded_num = round(num)
rounded_num1 = round(num, 2)

print(f'Rounded number: {rounded_num}')
print(f'Rounded by 2 decimal places: {rounded_num1}')

# abs(): Returns the absolute value of a number

num = -7
abs_num = abs(num)
print(f'Absolute value: {abs_num}')

# pow(): raises a number to the power of another or performs modular exponentiation.

num = pow(num, 2)
print(f'Power of number: {num}')

num = pow(num, 2, 5)  # (num ** 2) % 5
print(f'Modular exponentiation: {num}')
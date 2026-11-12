# Using while Loops
# Another type of loop you can use in Python is the while loop. This type of loop will repeat a block of code until the condition is False. Here is an example of using a while loop for a guessing game:
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number(1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You get it!')
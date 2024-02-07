# Creates an input prompt for the user to select the operation to perform.
choice = input('''
Please select the type of operation you want to perform:
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
''')


# Creates a first variable that is inputted by the user. In the form of an integer.
num_1 = int(input('Enter your first number: '))

# Creates a second variable that is inputted by the user. In the form of an integer.
num_2 = int(input('Enter your second number: '))


# Below is the operations to be preformed based on decision of user, using ELSE IF statements.
# the format() makes the output look better and formatted

# Addition
if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

# Subtraction
elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

# Multiplication
elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)

# Division
elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)

# Sends user an error message if entered operator is not valid    
else:
    print('Enter a valid operator, please run the program again.')
    
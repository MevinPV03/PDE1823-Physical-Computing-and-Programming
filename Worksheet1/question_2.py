# Program: Even or Odd Number
# This program checks whether a number entered by the user is even or odd.

# Get user input
number = float(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

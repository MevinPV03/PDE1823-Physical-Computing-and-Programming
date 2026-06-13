# Program: Total of 5 Numbers
# This program asks the user to enter 5 numbers
# and calculates their total using a loop.

# Initialize the total (accumulator variable)
total = 0

# Use a loop to get 5 numbers from the user
for i in range(1, 6):
    number = float(input(f"Enter number {i}: "))
    total = total + number  # Add each number to total

# Display the result
print(f"\nThe total is: {total}")
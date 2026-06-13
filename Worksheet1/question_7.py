# Program: Count Positive Numbers in a List
# This program asks the user to enter 6 numbers,
# stores them in a list, and counts how many are positive.

# Create an empty list
numbers = []

# Input 6 numbers from the user
for i in range(1, 7):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

# Initialize counter for positive numbers
positive_count = 0

# Loop through the list and count positives
for num in numbers:
    if num > 0:
        positive_count += 1

# Display results
print("\nThe numbers entered are:", numbers)
print(f"There are {positive_count} positive numbers.")
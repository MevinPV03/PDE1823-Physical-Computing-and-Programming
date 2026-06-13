# Program: Simple Shopping List
# This program asks the user to enter 5 shopping items
# and displays them as a list.

# Create an empty list to store items
shopping_list = []

# Use a loop to get 5 items from the user
for i in range(1, 6):
    item = input(f"Enter item {i}: ")
    shopping_list.append(item)

# Display the shopping list
print("\nYour shopping list is:")
for item in shopping_list:
    print(item)
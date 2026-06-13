# Function to calculate total price
def calculate_total(prices):
    total = 0
    for price in prices:
        total = total + price
    return total


# Function to apply discount
def apply_discount(total):
    if total > 1000:
        discount = total * 0.10
        final_total = total - discount
    else:
        final_total = total
    return final_total


# Main program
prices = []

num_items = int(input("How many items did the customer buy? "))

for i in range(1, num_items + 1):
    price = float(input(f"Enter price of item {i}: "))
    prices.append(price)

# Call functions
original_total = calculate_total(prices)
final_amount = apply_discount(original_total)

# Display results
print("\nOriginal total: Rs", original_total)
print("Final amount to pay: Rs", final_amount)
# Class definition for Product
class Product:
    # Constructor to initialize attributes
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Method to display product details
    def display_product(self):
        print(f"{self.name} | Price: Rs {self.price} | Stock: {self.stock}")

    # Method to sell product
    def sell(self, quantity):
        if quantity <= self.stock:
            total_amount = quantity * self.price
            self.stock -= quantity
            print("\nSale successful.")
            print(f"Amount for this sale: Rs {total_amount}")
            print(f"Remaining stock for {self.name}: {self.stock}")
            return total_amount
        else:
            print(f"\nNot enough stock available for {self.name}.")
            print(f"Current stock: {self.stock}")
            return 0


# Main program

# List to store products
products = []

# Variable to track total sales
total_sales = 0

# Input number of products
num_products = int(input("How many products do you want to enter? "))

# Loop to enter product details
for i in range(1, num_products + 1):
    print()
    name = input(f"Enter product {i} name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))

    # Create Product object and add to list
    product = Product(name, price, stock)
    products.append(product)

# Menu loop
while True:
    print("\nMenu:")
    print("1. Display products")
    print("2. Sell product")
    print("3. Exit")

    choice = int(input("Menu choice: "))

    if choice == 1:
        print("\nProduct List:")
        for i in range(len(products)):
            print(f"{i + 1}. ", end="")
            products[i].display_product()

    elif choice == 2:
        product_num = int(input("Enter product number to sell: "))
        if 1 <= product_num <= len(products):
            quantity = int(input("Enter quantity: "))
            # Call sell method and add to total sales
            total_sales += products[product_num - 1].sell(quantity)
        else:
            print("Invalid product number.")

    elif choice == 3:
        break

    else:
        print("Invalid choice. Please try again.")

# Final output
print(f"\nTotal sales amount: Rs {total_sales}")

print("\nRemaining Stock:")
for product in products:
    print(f"{product.name}: {product.stock} left")
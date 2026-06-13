# Program: Calculate Area of a Rectangle
# This program defines a function to compute the area of a rectangle
# and uses user input to calculate and display the result.

# Function to calculate area
def calculate_area(length, width):
    area = length * width
    return area


# Main program

# Get user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# Call the function
area = calculate_area(length, width)

# Display the result
print(f"\nThe area of the rectangle is: {area}")
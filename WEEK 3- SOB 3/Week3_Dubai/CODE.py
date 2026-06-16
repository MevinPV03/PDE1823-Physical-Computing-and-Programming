#Q1 – Get Day Function

def get_day(day_number):
    if day_number == 1:
        return "Monday"
    elif day_number == 2:
        return "Tuesday"
    elif day_number == 3:
        return "Wednesday"
    elif day_number == 4:
        return "Thursday"
    elif day_number == 5:
        return "Friday"
    elif day_number == 6:
        return "Saturday"
    elif day_number == 7:
        return "Sunday"
    else:
        return "Invalid day number"

# Example
num = int(input("Enter day number: "))
print("Day", num, "is", get_day(num))

#Q2 – cube() and divisible_by_three()

def cube(number):
    return number ** 3

def divisible_by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# Example usage
num = int(input("Enter number: "))
print(divisible_by_three(num))

#Q3 – Print Hours

for hour in range(6, 20):
    print(f"{hour}:00")

#Q4 – Medicine Reminder

for hour in range(6, 20):
    print(f"{hour}:00")
    if hour >= 8 and (hour - 8) % 4 == 0:
        print("take medicine")

#Q5 – Factorial Function

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter number: "))
print(f"Factorial of {num} is {factorial(num)}")

#Q6 – Square Root Table

import math

print("Number\tSquare root")

for num in range(0, 20, 2):
    print(num, "\t", format(math.sqrt(num), ".2f"))

#Q7 – Triangle Pattern

n = 5

# Upper part
for i in range(1, n + 1):
    print("* " * i)

# Lower part
for i in range(n, 0, -1):
    print("* " * i)

#Q8 – Triangle Function

def triangle(n):
    # Upper
    for i in range(1, n + 1):
        print("* " * i)

    # Lower
    for i in range(n, 0, -1):
        print("* " * i)

# Test
num = int(input("Enter number of lines: "))
triangle(num)

#Q9 – Fibonacci Function

def fib(n):
    a = 0
    b = 1

    for i in range(1, n):
        a, b = b, a + b

    return a

# Test
num = int(input("Enter n: "))
print("Fibonacci:", fib(num))
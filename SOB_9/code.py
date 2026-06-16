#OPTION 1: math
#library(Circle class )

import math  # The math module is imported so we can use built-in mathematical functions like pi.
             # The interpreter loads this module into memory, allowing access through 'math.'

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        return 2 * math.pi * self.radius

# Example usage
c1 = Circle(5)
print("Area:", c1.getArea())
print("Circumference:", c1.getCircumference())

#OPTION 2: random module

import random  # The random module is imported so we can generate random numbers.
               # Python loads it into memory so we can access its functions.

def randomlist(length):
    randlist = []
    for i in range(length):
        n = random.randint(1, 10)  # Using function from the random module
        randlist.append(n)
    return randlist

print(randomlist(5))

#OPTION 3 : urllib

import urllib.request  # This imports the urllib module used to access data from URLs.
                       # The interpreter loads it so we can use its functions like urlopen.

def main():
    url = input("Enter URL: ").strip()
    data = urllib.request.urlopen(url)  # Using module function
    content = data.read().decode()

    print("Content length:", len(content))

main()
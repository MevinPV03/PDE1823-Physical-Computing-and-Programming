'''
class Student:
    def __init__(self, name, age, programme):     #names etc are attributes
        self.name = name                          #self shows that name is for that specific class
        self.age = age
        self.programme = programme

    def introduce(self):                           #introduce() is a method
        print(f" My name is {self.name}.")
        print(f"I study {self.programme}.")

student1= Student("Aisha", 18, "Robotics")     #student1 is an object
student1.introduce()

'''

import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        return 2 * math.pi * self.radius

c1 = Circle()
print(c1.radius)
print(c1.getArea())

c1.setRadius(5)
print(c1.radius)
print(c1.getArea)



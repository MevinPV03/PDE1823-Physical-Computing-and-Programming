import math

class Circle:
    """
    This class represents a circle and provides methods
    to calculate its area and circumference.
    """

    def __init__(self, radius=1):
        self.radius = radius  # Initial state of the object

    def setRadius(self, radius):
        """This method modifies the radius of the circle."""
        self.radius = radius  # Modifying object state

    def getArea(self):
        """Returns the area of the circle."""
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.radius


# Instantiate object
c1 = Circle(3)

# Use methods
print("Initial radius:", c1.radius)
print("Initial area:", c1.getArea())

# Modify state using method
c1.setRadius(5)

# Show updated values
print("Updated radius:", c1.radius)
print("Updated area:", c1.getArea())
import math
from calculator import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"This is a circle with radius {self.radius}."


if __name__ == "__main__":
    # Test the class if run directly
    shape = Shape()
    print(shape)

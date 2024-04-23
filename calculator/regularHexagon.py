import math
from calculator import Shape

class RegularHexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2

    def get_perimeter(self):
        return 6 * self.side

    def __str__(self):
        return f"This is a regular hexagon with side {self.side}."


if __name__ == "__main__":
    # Test the class if run directly
    shape = Shape()
    print(shape)

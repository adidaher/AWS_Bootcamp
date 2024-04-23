from rectangle import Rectangle
from calculator import Shape
class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return super().get_area() * 0.5

    def __str__(self):
        return f"This is a triangle with base {self.length} and height {self.width}."


if __name__ == "__main__":
    # Test the class if run directly
    shape = Shape()
    print(shape)

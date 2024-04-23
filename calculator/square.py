# square.py
from rectangle import Rectangle
from calculator import Shape
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"This is a square with side {self.length}."
if __name__ == "__main__":
    # Test the class if run directly
    shape = Shape()
    print(shape)

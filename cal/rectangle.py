from calculator import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"This is a rectangle with length {self.length} and width {self.width}."
if __name__ == "__main__":
    # Test the class if run directly
    shape = Shape()
    print(shape)

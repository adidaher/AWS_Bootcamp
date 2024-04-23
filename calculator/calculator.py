
class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        return "This is a generic shape."
if __name__ == "__main__":
    # Test the class if run directly
    shape = Shape()
    print(shape)

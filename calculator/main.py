from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from regularHexagon import RegularHexagon


def main():
    rectangle = Rectangle(4, 6)
    print(rectangle)
    print("Area:", rectangle.get_area())
    print("Perimeter:", rectangle.get_perimeter())

    square = Square(5)
    print(square)
    print("Area:", square.get_area())
    print("Perimeter:", square.get_perimeter())

    triangle = Triangle(3, 4)
    print(triangle)
    print("Area:", triangle.get_area())
    print("Perimeter:", triangle.get_perimeter())

    circle = Circle(5)
    print(circle)
    print("Area:", circle.get_area())
    print("Perimeter:", circle.get_perimeter())

    hexagon = RegularHexagon(4)
    print(hexagon)
    print("Area:", hexagon.get_area())
    print("Perimeter:", hexagon.get_perimeter())

if __name__ == "__main__":
    main()
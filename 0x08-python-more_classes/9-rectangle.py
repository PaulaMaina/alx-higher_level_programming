#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Initializes a Rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Args:
                width: width of a rectangle
                height: height of a rectangle
            Raises:
                TypeError: If width or height is not an int
                ValueError: If width or height is < 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width of a rectangle"""
        return self.__width

    @property
    def height(self):
        """Height of a rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Assigns value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Assigns value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns a rectangle with hashes"""
        if self.__width == 0 or self.__height == 0:
            return ""
        if self.print_symbol:
            symbol = "{}".format(self.print_symbol)
        else:
            symbol = "{}".format(Rectangle.print_symbol)
        return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string rep.  of an instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message before an instance is destroyed"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Calculates the larger rectangle based ont he areas"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance where width equals the height"""
        return Rectangle(size, size)

#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """A subclass of the Base class with dimension and position attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the attributes of the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets and validates the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets and validates the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets and validates the x position of the Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets and validates the y position of the Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")

    def area(self):
        """Calculates the area of a Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Displays a rectangle shape using '#'s"""
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.width] * self.height))

    def __str__(self):
        """Displays the string representation of the Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes"""
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for a in range(len(args)):
                setattr(self, attrs[a], args[a])
            return
        for b, c int kwargs.items():
            if hasattr(self, b):
                setattr(self, b, c)

    def to_dictionary(self):
        """Returns the dictionary representaion of the Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }

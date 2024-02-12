#!/usr/bin/python3
"""Square class definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits the size argument from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initiates the class attributes of Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Displays the string representation of the instance of Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width
                )

    def update(self, *args, **kwargs):
        """Updates the Square attributes"""
        attrs = ["id", "size", "x", "y"]

        if args:
            for a in range(len(args)):
                setattr(self, attrs[a], args[a])
            return
        for b, c in kwargs.items():
            if hasattr(self, b):
                setattr(self, b, c)

    def to_dictionary(self):
        """Displays the dictionary representation of the Square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

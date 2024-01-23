#!/usr/bin/python3
"""Square class definition with a private attribute size"""


class Square():
    """Definition of 'Square'"""
    def __init__(self, size=0, position=(0, 0)):
        """Init an object of square with a private instance attribute 'size'

            Args:
                size: size of a square
                position: a tuple of the sqaure's position

            Raises:
                TypeError: Size is not an integer
                ValueError: Size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if isinstance(position, tuple) and len(position) == 2 and\
                isinstance(position[0], int) and isinstance(position[1], int)\
                and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the size of a square

            Returns:
                The size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets square size with a value

            Args:
                value: value to be assigned to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square with '#'s"""
        if self.__size == 0:
            print()
            return
        print("{}".format("\n" * self.__position[1]), end="")
        print("{}".format("\n".join(
            [" " * self.__position[0] + "#" * self.__size] * self.__size)))

    @property
    def position(self):
        """Retrieves the position of the square

            Returns:
                Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the square

            Args:
                value: value to be assigned to position
        """
        if isinstance(value, tuple) and len(value) == 2 and\
                isinstance(value[0], int) and isinstance(value[1], int) and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """Returns a string same as the one prints in my_print function"""
        string = ""
        if self.__size == 0:
            return string
        string += "{}".format("\n" * self.__position[1])
        string += "{}".format("\n".join(
            [" " * self.__position[0] + "#" *self.__size] * self.__size))
        return string

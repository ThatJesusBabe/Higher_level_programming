#!/usr/bin/python3
""" create square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
        size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size <= 0:
            print()
        if self.size > 0:
            for i in range(0, self.__size):
                if self.__position[0] > 0 and type(self.__position[0] == 'int'):
                    print("_" * self.__position[0], end='')
                for j in range(0, self.__size):
                    print("#", end='')
                if self.position[1] < 0:
                    print("")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """

        if len(value) < 2 or type(value) != 'tuple' or value == '':
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != 'int' or type(value[1]) != 'int':
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

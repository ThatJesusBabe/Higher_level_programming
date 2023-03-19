#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
"""there is an error here"""
varia = "position"
my_square = Square(3, varia)

print("--")
"""there is an error here"""
my_square = Square(3, (1, ))

print("--")
"""there is an error here"""
my_square = Square(3, (1, -3))

print("--")
"""there is an error here"""
lett = "3"
my_square = Square(3, (1, lett))

print("--")

mysquare = Square(3)
mysquare.my_print()

print("--")

mysquare = Square(3, (0, 0))
mysquare.my_print()

print("--")
"""there is an error here"""
mysquare = Square(3, (1, 0))
mysquare.my_print()

print("--")
"""there is an error here"""
mysquare = Square(3, (0, 1))
mysquare.my_print()

print("--")
"""there is an error here"""
mysquare = Square(0, (10, 3))
mysquare.my_print()

print("--")
"""there is an error here"""
mysquare = Square(5, (3, 2))
mysquare.my_print()

print("--")

mysquare = Square(3, (1, 1))
mysquare.my_print()

print("--")


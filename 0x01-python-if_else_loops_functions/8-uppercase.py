#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            alp = ord(i) - 32
            print(chr(alp), end="")
        else:
            print(i, end="\n")

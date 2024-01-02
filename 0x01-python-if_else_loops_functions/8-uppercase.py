#!/usr/bin/python3
def uppercase(str):
    capital = 0
    for letter in str:
        if (ord(letter) >= ord('a') and ord(letter) <= ord('z')):
            capital = 32
        else:
            capital = 0
        print("{:letter}".format(ord(letter) - capital), end='')
    print("")


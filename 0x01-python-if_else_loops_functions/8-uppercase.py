#!/usr/bin/python3
def uppercase(str):
    capital = 0
    for c in str:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            capital = 32
        else:
            capital = 0
        print("{:c}".format(ord(c) - capital), end='')
    print("")

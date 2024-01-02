#!/usr/bin/python3
for a in range(10):
    for b in range(10):
        if (a == 8 and b == 9):
            print("{}".format(str(a) + str(b)))
        elif (b > a):
            print("{}".format(str(a) + str(b)), end=", ")

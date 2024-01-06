#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    evenList = my_list[:]

    for num in evenList:
        if (num % 2) == 0:
            evenList[num] = True
        else:
            evenList[num] = False

    return evenList

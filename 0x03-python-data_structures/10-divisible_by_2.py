#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    evenList = []

    for num in my_list:
        if (num % 2) == 0:
            evenList.append(True)
        else:
            evenList.append(False)

    return evenList

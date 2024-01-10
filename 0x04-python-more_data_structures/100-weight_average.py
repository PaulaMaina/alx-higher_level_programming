#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        total_weight = 0
        tally = 0
        for elem in my_list:
            x = list(elem)
            value = 1
            for y in x:
                value *= y
            total_weight += value
            tally += x[1]
        return total_weight/tally

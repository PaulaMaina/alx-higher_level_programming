#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
my_list2 = []
list_result = divisible_by_2(my_list)
list_result2 = divisible_by_2(my_list2)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

print("Length: {}".format(len(list_result)))
for i in list_result:
    print(i, end=", ")

print(list_result2)

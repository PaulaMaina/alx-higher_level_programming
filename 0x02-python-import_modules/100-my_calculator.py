#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if (len(argv[1:])) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]

    if sign not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if sign == ops[0]:
            result = add(a, b)
        elif sign == ops[1]:
            result = sub(a, b)
        elif sign == ops[2]:
            result = mul(a, b)
        elif sign == ops[3]:
            result = div(a, b)

    print("{} {} {} = {}".format(a, sign, b, result))

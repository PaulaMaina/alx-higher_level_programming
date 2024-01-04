#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculator_102 import add, sub

    if (a < b):
        c = (add(a, b))
        for d in range(4, 6):
            c = add(c, d)
        return c
    else:
        return sub(a, b)

    if __name__ == "__main__":
        import dis

        dis.dis(magic_calculation)

#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) == str):
        ind = len(roman_string) - 1
        digit = []
        romans = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                }
        val = romans[roman_string[ind]]
        while ind >= 0:
            sym = roman_string[ind]

            if romans[roman_string[ind - 1]] < romans[sym] and ind != 0:
                digit.append(romans[sym] - romans[roman_string[ind - 1]])
                ind -= 2
            elif romans[roman_string[ind - 1]] >= romans[sym] and ind != 0:
                digit.append(romans[sym])
                val = romans[sym]
                ind -= 1
            elif ind == 0:
                digit.append(romans[sym])
                break
        return sum(digit)
    else:
        return 0

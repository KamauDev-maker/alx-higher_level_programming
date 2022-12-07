#!/usr/bin/python3
roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000
def roman_to_int(roman_string):
    sum = 0
    n = len(roman_string)
    i = 0
    while i < n :
        if (i != n -1 and roman[roman_string[i]] < roman[roman_string[i + 1]]):
            sum += roman[roman_string[i + 1]] - roman[roman_string[i]]
            i += 2
            continue
        else:
            sum += roman[roman_string[i]]
        i += 1
    return sum

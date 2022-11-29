#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if ord(i) >= ('a') and ord(i) <= ('z'):
            result += chr(ord(i) - 32)
        else:
            result += i
        print("{}".format(result))

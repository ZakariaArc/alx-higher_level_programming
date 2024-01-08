#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)

#!/bin/python3

import os


def counting_valleys(n, s):
    _valleys = 0
    _level = 0

    for i in range(0, n):
        if s[i] == 'U':
            _level += 1
            if _level == 0:
                _valleys += 1
        else:
            _level -= 1

    return _valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

import os


def jumping_on_clouds(n, c):
    _jumps = 0
    _index = 0
    while _index < n - 1:
        if c.get(_index + 2) != 1:
            _index += 1
        _index += 1
        _jumps += 1

    return _jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

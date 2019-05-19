#!/bin/python3

# https://www.hackerrank.com/challenges/2d-array/problem

import os


def hourglass_sum(arr):
    _max = -63
    for row in range(0, 4):
        for col in range(0, 4):
            _sum = sum(arr[row][col:col + 3]) + \
                   sum(arr[row + 2][col:col + 3]) + \
                   arr[row + 1][col + 1]
            if _sum > _max:
                _max = _sum

    return _max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

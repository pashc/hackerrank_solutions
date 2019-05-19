#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

import os


def rot_left(n, d, a):
    rotated = []

    for i in range(n):
        rotated_index = (i + (n - d)) % n
        rotated.insert(rotated_index, a[i])

    return rotated


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rot_left(n, d, a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

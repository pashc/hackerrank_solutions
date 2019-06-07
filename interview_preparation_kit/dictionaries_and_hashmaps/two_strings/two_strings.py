#!/bin/python3

import os


def two_strings(s1, s2):
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in s1 and c in s2:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = two_strings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

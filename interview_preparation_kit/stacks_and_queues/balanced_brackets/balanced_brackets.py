#!/bin/python3

import os


def is_balanced(s):
    closes = {a: b for a, b in zip(')}]', '({[')}
    stack = []

    for c in s:
        if stack and closes.get(c) == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return len(stack) == 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        if is_balanced(s):
            result = 'YES'
        else:
            result = 'NO'

        fptr.write(result + '\n')

    fptr.close()

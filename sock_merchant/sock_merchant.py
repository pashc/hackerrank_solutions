#!/bin/python3

import os


# time and space in O(n)
def sock_merchant(n, ar):
    _set = set()
    _count = 0
    for i in range(0, n):
        e = ar[i]
        if e in _set:
            _set.remove(e)
            _count += 1
        else:
            _set.add(e)
    return _count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

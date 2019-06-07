#!/bin/python3

import os


def minimum_swaps(n, arr):
    visited = [*enumerate(arr)]
    visited.sort(key=lambda it: it[1])

    count = 0
    i = 0

    while i < n:
        j = visited[i][0]
        if j == i:
            i += 1
            continue

        tmp = visited[i]
        visited[i] = visited[j]
        visited[j] = tmp

        count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(n, arr)

    fptr.write(str(res) + '\n')

    fptr.close()

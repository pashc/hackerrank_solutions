#!/bin/python3

# https://www.hackerrank.com/challenges/new-year-chaos/problem


def minimum_bribes(n, q):
    i = n - 1
    bribes = 0
    while i >= 0:
        if q[i] - (i + 1) > 2:
            return 'Too chaotic'
        j = max(0, q[i] - 2)
        while j < i:
            if q[j] > q[i]:
                bribes += 1
            j += 1
        i -= 1

    return bribes


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimum_bribes(n, q))

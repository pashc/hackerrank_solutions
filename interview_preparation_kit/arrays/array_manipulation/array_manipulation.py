# !/bin/python3

import os


def array_manipulation(n, queries):
    arr = [0] * (n + 1)
    for q in queries:
        start, end, incr = q[0], q[1], q[2]

        arr[start - 1] += incr
        if end <= n + 1:
            arr[end] -= incr

    max_value, current = 0, 0
    for i in arr:
        current += i
        if max_value < current:
            max_value = current

    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

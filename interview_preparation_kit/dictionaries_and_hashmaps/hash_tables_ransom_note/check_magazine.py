#!/bin/python3


def check_magazine(magazine, note):
    included_table = {}

    for word in magazine:
        if word in included_table.keys():
            included_table[word] += 1
        else:
            included_table[word] = 1

    for word in note:
        if word not in included_table.keys():
            return "No"

        counter = included_table.get(word) - 1
        if counter == 0:
            included_table.pop(word)
        else:
            included_table[word] = counter

    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(check_magazine(magazine, note))

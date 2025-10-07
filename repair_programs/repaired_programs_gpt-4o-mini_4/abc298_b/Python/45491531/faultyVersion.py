#!/usr/bin/env python3

def r(a):
    a = [row[::-1] for row in a]  # Reverse each row (left to right)
    return list(map(list, zip(*a)))  # Transpose the matrix

n = int(input())
a = [list(input().split()) for _ in range(n)]
b = [list(input().split()) for _ in range(n)]

f = True
for _ in range(3):
    a = r(a)

    f = True
    for al, bl in zip(a, b):
        for av, bv in zip(al, bl):
            if av == "1":
                if bv == "0":
                    f = False
                    break
        if not f:
            break

    if f:
        print("Yes")
        exit()
print("No")
from collections import deque
N = int(input())
S = input()

L = deque()
temp = []
for s in S:
    if s != "(" and s != ")":
        temp.append(s)
    elif s == "(":
        if temp:
            L.append("".join(temp))
        temp.clear()
        temp.append("(")
    elif s == ")":
        if temp:
            L.append("".join(temp))
            temp.clear()
        if L and L[-1][0] == "(":
            L.pop()
        else:
            continue  # Changed this line to avoid adding unmatched closing parentheses

if temp:
    L.append("".join(temp))

print("".join(L))
S = input()
num = set(range(1, 10))

for s in S:
    num.discard(int(s))

print(*num)
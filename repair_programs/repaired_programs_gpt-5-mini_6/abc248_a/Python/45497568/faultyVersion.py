S = input()
num = set(range(10))

for s in S:
    num.discard(int(s))

print(*num)
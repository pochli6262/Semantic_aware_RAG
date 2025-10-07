S = input()
num = set([i for i in range(10)])

for s in S:
    num.discard(int(s))

print(*num)
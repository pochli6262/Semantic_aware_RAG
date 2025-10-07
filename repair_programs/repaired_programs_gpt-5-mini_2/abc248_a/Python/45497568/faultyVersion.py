S = input()
num = set([i for i in range(1, 10)])

for s in S.split():
    num.discard(int(s))

print(*num)

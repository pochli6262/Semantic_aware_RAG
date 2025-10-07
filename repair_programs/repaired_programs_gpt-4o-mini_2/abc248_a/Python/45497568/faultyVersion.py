S = input()
num = set([i for i in range(1, 10)])

for s in S:
    if s.isdigit() and int(s) in num:
        num.discard(int(s))

print(*num)
N = int(input())

Z = set()

count = 0
for i in range(N):
    S = input()
    if S in Z or S[::-1] in Z:
        continue
    Z.add(S)
    Z.add(S[::-1])
    count += 1

print(count)
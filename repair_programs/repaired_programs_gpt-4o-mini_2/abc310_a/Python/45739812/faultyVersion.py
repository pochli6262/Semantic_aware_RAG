N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

res = P

for d in D:
    if (p := P - d + Q) < res:
        res = p

print(res)
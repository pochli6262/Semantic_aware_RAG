N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

res = P

for d in D:
    p = P - Q + d
    if p < res:
        res = p

print(res)
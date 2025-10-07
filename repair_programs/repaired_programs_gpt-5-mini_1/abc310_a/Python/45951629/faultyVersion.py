N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

ans = 10**18
for i in range(N):
    ret = P - Q + D[i]
    ans = min(ans, ret)

print(ans)

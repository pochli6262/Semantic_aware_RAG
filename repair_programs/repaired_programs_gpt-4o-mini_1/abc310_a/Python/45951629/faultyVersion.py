N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

ans = P
for i in range(N):
    ret = P - D[i] + Q
    ans = min(ans, ret)

print(ans)
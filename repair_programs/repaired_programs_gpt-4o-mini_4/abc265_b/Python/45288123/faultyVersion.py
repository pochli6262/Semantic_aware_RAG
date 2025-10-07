from collections import defaultdict

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]

d = defaultdict(int)
for x, y in XY:
    d[x] = y

now = 1
while now != N:
    if T < A[now-1]:
        print('No')
        exit()
    T -= A[now-1]
    now += 1

    T += d[now]
    # print(T)

print('Yes')
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
B = []
for i in range(M):
    B.append(tuple(map(int, input().split())))

from collections import deque
queA = deque(A)
B.sort(key=lambda x: x[0])
queB = deque(B)

ans = "Yes"
nowT = T
nowP = 1
S = set([row[0] for row in B])
for i in range(N-1):
    p = queA.popleft()
    while nowP in S:
        pt = queB.popleft()
        nowT += pt[1]
        nowP += 1

    if nowT >= p:
        nowT -= p
        nowP += 1
    else:
        ans = "No"
        break

print(ans)
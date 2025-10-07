N = int(input())
A = list(map(int,input().split()))

res = []
SUM = 0
for i in range(len(A)):
    SUM += A[i]
    if (i + 1)%7==0:
        res.append(SUM)
        SUM = 0

print(res)
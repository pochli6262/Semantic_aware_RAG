N = int(input())
A = list(map(int,input().split()))

res = [0]*((N + 6) // 7)
SUM = 0
index = 0
for i in range(len(A)):
    SUM += A[i]
    if (i + 1)%7==0:
        res[index] = SUM
        index += 1
        SUM = 0

print(res)
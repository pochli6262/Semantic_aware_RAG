N = int(input())
A = list(map(int,input().split()))

res = [0]*((N + 6) // 7)
SUM = 0
for i in range(len(A)):
    SUM += A[i]
    if (i + 1) % 7 == 0:
        res[i // 7] = SUM
        SUM = 0

if SUM > 0:  # This handles any leftover sum that doesn't fill a complete 7
    res[len(res) - 1] = SUM

print(res)
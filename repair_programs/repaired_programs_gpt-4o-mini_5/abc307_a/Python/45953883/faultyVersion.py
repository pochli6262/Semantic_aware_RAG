N = int(input())
A = list(map(int,input().split()))

res = [0]*N
for i in range(N):
    res[i] = sum(A[i*7:(i+1)*7])

print(res)
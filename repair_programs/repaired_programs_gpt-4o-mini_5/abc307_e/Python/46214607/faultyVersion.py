N,M=map(int,input().split())
mod=998244353

if N > M:
    answer = (M - 1) * pow(M - 2, N - 1, mod)
else:
    answer = 0 if N == M else (M - 1) * (M ** (N - 2))
print(answer % mod)
N,M=map(int,input().split())
mod=998244353

if M == 1 and N > 1:
    print(0)
else:
    answer = (M - 1) * pow(M, N - 1, mod) % mod
    print(answer)
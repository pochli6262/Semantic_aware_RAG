N,M=map(int,input().split())
mod=998244353

answer=(M-1)*((M-2)**(N-1))%mod
print(answer)
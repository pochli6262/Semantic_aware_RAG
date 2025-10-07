N,M=map(int,input().split())
mod=998244353
answer=((M-1) * (-1)**(N%2)) % mod + pow(M-1,N,mod)) % mod
print(answer)
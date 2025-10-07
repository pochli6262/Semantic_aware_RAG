N, K = map(int,input().split())
A=list(map(int,input().split()))
Q=int(input())
S = [[0] for i in range(K)]
for i in range(N):
    S[i%K].append(S[i%K][-1]+A[i])
    
for i in range(Q):
    l, r = map(lambda x:int(x)-1,input().split())
    s=set()
    for k in range(K):
        s.add(S[k][(r-k)//K+1] - S[k][max(0, (l-k)//K)])
    if len(s)==1:
        print('Yes')
    else:
        print('No')
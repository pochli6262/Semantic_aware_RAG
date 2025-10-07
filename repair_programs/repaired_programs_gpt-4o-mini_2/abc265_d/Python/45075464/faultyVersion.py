from bisect import bisect_left as bl
N,P,Q,R = list(map(int,input().split()))
A = list(map(int,input().split()))
asum = [0]
for n in range(N):
    asum.append(asum[-1]+A[n])
for x in range(N):
    a = asum[x]
    y = bl(asum,P+a)
    if y>=N or asum[y]-a!=P or (y<N and asum[y]-asum[x]!=P) : continue
    a = asum[y]
    z = bl(asum,Q+a)
    if z>=N or asum[z]-a!=Q or (z<N and asum[z]-asum[y]!=Q): continue
    a = asum[z]
    w = bl(asum,R+a)
    if w>=N or asum[w]-a!=R or (w<N and asum[w]-asum[z]!=R): continue
    print("Yes")
    break
else:
    print("No")
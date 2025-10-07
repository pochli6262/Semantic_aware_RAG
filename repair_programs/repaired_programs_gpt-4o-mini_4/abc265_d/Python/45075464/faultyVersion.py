from bisect import bisect_left as bl
N,P,Q,R = list(map(int,input().split()))
A = list(map(int,input().split()))
asum = [0]
for n in range(N):
    asum.append(asum[-1]+A[n])
for x in range(N):
    a = asum[x]
    y = bl(asum,P+a) - 1
    if y>=N or asum[y+1]-a!=P : continue
    a = asum[y+1]
    z = bl(asum,Q+a) - 1
    if z>=N or asum[z+1]-a!=Q : continue
    a = asum[z+1]
    w = bl(asum,R+a) - 1
    if w>=N or asum[w+1]-a!=R : continue
    print("Yes")
    break
else:
    print("No")
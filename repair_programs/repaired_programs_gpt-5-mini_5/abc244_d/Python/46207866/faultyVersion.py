S1,S2,S3 = input().split()
T1,T2,T3 = input().split()
cnt = (lambda p: sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) - ((S1!=T1)+(S2!=T2)+(S3!=T3)))(( [S1,S2,S3].index(T1), [S1,S2,S3].index(T2), [S1,S2,S3].index(T3) ))
if S1 != T1:
    cnt += 1
if S2 != T2:
    cnt += 1
if S3 != T3:
    cnt += 1
print("Yes" if cnt%2==0 else "No")
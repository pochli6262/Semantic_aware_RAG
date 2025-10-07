S1,S2,S3 = input().split()
T1,T2,T3 = input().split()
cnt = ((({S1:1,S2:2,S3:3}[T1] > {S1:1,S2:2,S3:3}[T2]) + ({S1:1,S2:2,S3:3}[T1] > {S1:1,S2:2,S3:3}[T3]) + ({S1:1,S2:2,S3:3}[T2] > {S1:1,S2:2,S3:3}[T3])) + ((S1!=T1) + (S2!=T2) + (S3!=T3)))%2
if S1 != T1:
    cnt += 1
if S2 != T2:
    cnt += 1
if S3 != T3:
    cnt += 1
print("Yes" if cnt%2==0 else "No")
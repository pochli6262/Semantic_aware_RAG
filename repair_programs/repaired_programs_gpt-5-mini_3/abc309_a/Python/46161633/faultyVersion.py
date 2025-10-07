A,B=map(int, input().split())
if A%3==0 and B==A+1:
    print('No')
elif abs(A-B)==1 or abs(A-B)==3:
    print('Yes')
else:
    print('No')
A,B=map(int, input().split())
if A%3==0 and B==A+1:
    print('No')
elif B==A+1 or B==A+3:
    print('Yes')
else:
    print('No')
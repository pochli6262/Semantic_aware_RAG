a,b,c,x=list(map(int,input().split()))
ans=1.0
if x>A and x<=b:
    ans=c/(b-(A+1)+1)
elif x>b:
    ans=0.0
print('%.10f'%ans)
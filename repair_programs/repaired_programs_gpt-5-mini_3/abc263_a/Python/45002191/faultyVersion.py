x=list(map(int,input().split()))
if len(x) == 3 and len(set(x))==2:
    print("Yes")
else:
    print("No")
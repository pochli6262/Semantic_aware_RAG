x=list(map(int,input().split()))
if len(set(x))==2 and all(x.count(v)==2 for v in set(x)):
    print("Yes")
else:
    print("No")
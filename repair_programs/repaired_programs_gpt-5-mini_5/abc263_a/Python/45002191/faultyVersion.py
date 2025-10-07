x=list(map(int,input().split()))
if len(set(x))==2 and sorted([x.count(i) for i in set(x)])==[2,3]:
    print("Yes")
else:
    print("No")
x=list(map(int,input().split()))
if sorted([x.count(v) for v in set(x)])==[2,3]:
    print("Yes")
else:
    print("No")

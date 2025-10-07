a,b=map(int,input().split())
if (a-1)//3 == (b-1)//3 and abs(a-b) == 1:
  print("Yes")
else:
  print("No")
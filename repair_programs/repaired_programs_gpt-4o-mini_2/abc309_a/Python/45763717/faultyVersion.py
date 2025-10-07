a,b=map(int,input().split())
if not (a in {3, 4} and b in {3, 4}) and not (a in {6, 7} and b in {6, 7}) and abs(a-b) in [1,3]:
  print("Yes")
else:
  print("No")
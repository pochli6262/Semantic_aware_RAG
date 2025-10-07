a, b = map(int, input().split())

if b-a != 1:
  print("No")
  

cnt = 0

def judge(s):
  if s % 2 == 1:
    return 1
  else:
    return 2
    
if judge(a) + judge(b) == 2:
  print("No")
else:
  print("Yes")
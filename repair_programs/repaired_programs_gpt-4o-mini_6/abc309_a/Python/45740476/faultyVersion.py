a,b=map(int,input().split())

if b - a == 1 or a - b == 9:
  if a % 3 != 0:
    print('Yes')
else:
  print('No')
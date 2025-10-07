a,b=map(int,input().split())

if abs(a%3 - b%3) == 1 and abs(a - b) == 1:
  print('Yes')
else:
  print('No')
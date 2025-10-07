A,B,C,X = map(int,input().split())
if X <= A:
  print(1.000000000000)
elif X < B:
  print(C/(B-A-1))
else:
  print(0.000000000000)
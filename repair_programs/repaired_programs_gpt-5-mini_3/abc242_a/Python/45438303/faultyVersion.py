A,B,C,X = map(int,input().split())
if X <= A:
  print(1.000000000000)
elif X < B:
  print("{:.12f}".format(C/(B-A)))
else:
  print(0.000000000000)
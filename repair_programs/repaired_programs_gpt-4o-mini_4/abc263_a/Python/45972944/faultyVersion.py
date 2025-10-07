from collections import defaultdict

count = defaultdict(int)

A=list(map(int, input().split()))

for i in range(len(A)):
  count[A[i]] += 1

a = count.values()
a = list(a)

if sorted(a) == [2, 3]:
  print("Yes")
else:
  print("No")
from collections import defaultdict

count = defaultdict(int)

A=list(map(int, input().split()))

for i in range(len(A)):
  count[A[i]] += 1

a = list(count.values())

if len(count) != 2 or sorted(a) != [2, 3]:
  print("No")
else:
  print("Yes")
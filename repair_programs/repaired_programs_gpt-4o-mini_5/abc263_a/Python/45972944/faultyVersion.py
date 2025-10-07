from collections import defaultdict

count = defaultdict(int)

A=list(map(int, input().split()))

for i in range(len(A)):
  count[A[i]] += 1

a = list(count.values())

if len(a) != 2:
  print("No")
elif 3 in a and 2 in a:
  print("Yes")
else:
  print("No")
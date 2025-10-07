from collections import defaultdict

count = defaultdict(int)

A=list(map(int, input().split()))

for i in range(len(A)):
  count[A[i]] += 1

a = count.values()
a = list(a)

if  2 < len(count.values()):
  print("No")
elif 3 in a:
  print("YES")
else:
  print("No")
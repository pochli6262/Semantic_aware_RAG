import numpy

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

SA = numpy.cumsum(A)
sa_set = set(SA)  # Fixed line: Instead of adding each element to the set in a loop, create a set directly from SA.
for sa in SA:
  if sa + P in sa_set and sa + P + Q in sa_set and sa + P + Q + R in sa_set:
    print("Yes")
    exit()
print("No")
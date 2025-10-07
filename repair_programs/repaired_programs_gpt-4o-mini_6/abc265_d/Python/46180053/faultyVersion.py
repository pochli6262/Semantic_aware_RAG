import numpy

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

SA = numpy.cumsum(A)
sa_set = set(SA)

for i in range(N):
  if SA[i] + P in sa_set and SA[i] + P + Q in sa_set and SA[i] + P + Q + R in sa_set:
    print("Yes")
    exit()
print("No")
n, x = map(int, input().split())
A = [0 for _ in range(n)]
B = [0 for _ in range(n)]
for i in range(n):
  A[i], B[i] = map(int, input().split())

# dp[i][j] -> whether it's possible to make sum j using first i kinds of coins
# initialize
DP = [[False for _ in range(x + 1)] for _ in range(n + 1)]
for i in range(n + 1):
  DP[i][0] = True

for i in range(n):
  for j in range(x + 1):
    for k in range(B[i] + 1):
      if DP[i][j]:
        if j + (k * A[i]) <= x:
            DP[i + 1][j + (k * A[i])] = True

if DP[-1][-1]:
  print("Yes")
else:
  print("No")
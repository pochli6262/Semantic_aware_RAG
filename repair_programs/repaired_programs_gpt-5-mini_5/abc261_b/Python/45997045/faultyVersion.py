n = int(input())
a = [list(input()) for _ in range(n)]
b = []
for i in range(n):
  tmp = []
  for j in range(n):
    tmp.append(a[j][i])
  b.append(tmp)
ans = "correct"
for i in range(n):
  for j in range(n):
    if i == j:
      continue
    if a[i][j] == b[i][j] == 'D':
      continue
    if (a[i][j] == 'W' and b[i][j] != 'L') or (a[i][j] == 'L' and b[i][j] != 'W') or (a[i][j] == 'D' and b[i][j] != 'D'):
      ans = "incorrect"
      break
print(ans)
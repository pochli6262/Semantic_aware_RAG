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
    if a[i][j] == 'D' and b[j][i] == 'D':
      continue
    if a[i][j] == 'W' and b[j][i] != 'L':
      ans = "incorrect"
      break
    if a[i][j] == 'L' and b[j][i] != 'W':
      ans = "incorrect"
      break
print(ans)
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
    if a[i][j] == b[j][i] == 'D':
      continue
    if a[i][j] == b[j][i]:
      ans = "incorrect"
      break
print(ans)
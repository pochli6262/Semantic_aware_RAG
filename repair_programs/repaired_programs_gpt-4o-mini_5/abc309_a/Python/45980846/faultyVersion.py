grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = list(map(int, input().split()))
for i in range(3):
  for j in range(2):
    if (a[0] == grid[i][j] and a[1] == grid[i][j+1]):
      exit(print("Yes"))
print("No")
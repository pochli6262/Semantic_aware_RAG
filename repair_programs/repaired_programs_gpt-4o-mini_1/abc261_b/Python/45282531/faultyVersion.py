N = int(input())
A = [list(input()) for _ in range(N)]

for i in range(N):
  for j in range(N):
    if (A[i][j] == 'W' and A[j][i] =='L') or (A[i][j] == 'L' and A[j][i] =='W'):  
      print('incorrect')
      exit()
print('correct')
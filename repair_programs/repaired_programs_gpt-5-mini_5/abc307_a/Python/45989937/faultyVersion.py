n = int(input())
s = list(map(int,input().split()))

for i in range(n):
  ans = 0
  for l in range(7):
    ans += s[7*i + l]

  print(str(ans),"",end = "")

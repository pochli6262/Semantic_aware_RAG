n, k = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
for i in range(min(k, n)):
  print(s[i])
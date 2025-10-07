n, k = map(int, input().split())
s = [input() for _ in range(n)]
s.sort()
k = min(k, n)
for i in range(k):
  print(s[i])
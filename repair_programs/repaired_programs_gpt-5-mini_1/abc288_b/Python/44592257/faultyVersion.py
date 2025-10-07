n, k = map(int, input().split())
s = [input() for _ in range(n)]
s.sort(reverse=True)
for i in range(k):
  print(s[i])
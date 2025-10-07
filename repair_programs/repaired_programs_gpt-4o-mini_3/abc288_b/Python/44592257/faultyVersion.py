n, k = map(int, input().split())
s = [input() for _ in range(n)]
s = sorted(set(s))
for i in range(k):
  print(s[i])
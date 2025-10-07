n, k = map(int, input().split())
s = [input() for _ in range(n)]
s_top_k = s[:k]
s_top_k.sort()
for i in range(k):
  print(s_top_k[i])
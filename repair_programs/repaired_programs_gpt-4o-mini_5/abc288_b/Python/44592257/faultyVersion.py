n, k = map(int, input().split())
s = [input() for _ in range(n)]

# Get top K participants based on their input order
# Sorting only the selected top K participants
for i in range(k):
  print(s[i])

# Sort and print lexicographically
sorted_top_k = sorted(s[:k])
for nickname in sorted_top_k:
  print(nickname)
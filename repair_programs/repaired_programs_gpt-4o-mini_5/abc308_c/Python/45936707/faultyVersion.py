import sys

n = int(input())
ans = []
for i in range(1, n + 1):
	A, B = map(int, sys.stdin.readline().strip().split())
	sum = A + B
	res = A / (sum)
	ans.append((res, i))

ans.sort(key=lambda x: (-x[0], x[1]))
for i in range (0, len(ans)):
	print(ans[i][1], end = " ")
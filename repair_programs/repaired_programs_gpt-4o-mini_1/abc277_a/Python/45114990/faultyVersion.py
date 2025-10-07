n, x = map(int, input().split())
p = list(map(int, input().split()))
print(p.index(x) if x in p else -1)
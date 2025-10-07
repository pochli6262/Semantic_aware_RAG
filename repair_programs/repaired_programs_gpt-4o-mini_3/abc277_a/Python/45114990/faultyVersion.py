n, x = map(int, input().split())
p = list(map(int, input().split()))
if x in p:
    print(p.index(x))
else:
    print(-1)
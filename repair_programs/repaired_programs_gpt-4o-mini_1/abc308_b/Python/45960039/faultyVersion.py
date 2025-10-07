n, m = map(int, input().split())
c = input().split()
d = input().split()
p = list(map(int, input().split()))
ds = {d[i]: p[i + 1] for i in range(m)}
s = 0
for i in c:
    if i not in ds:
        print(p[0])
    else:
        s += ds[i]
print(s)
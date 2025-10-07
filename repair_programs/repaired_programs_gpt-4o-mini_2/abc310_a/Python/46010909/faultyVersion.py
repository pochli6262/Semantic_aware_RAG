n, p, q = map(int,input().split())
d_list = [int(e) for e in input().split()]

a = min(d_list)

print(max(min(p - q + a, p), 0))
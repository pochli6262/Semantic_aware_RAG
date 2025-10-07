n, p, q = map(int,input().split())
d_list = [int(e) for e in input().split()]

a = max(d_list)

print(min(p-q+a,p))
n, p, q = map(int, input().split(' '))
d = list(map(int, input().split(' ')))
print(min(p, max(0, p - q + min(d))))
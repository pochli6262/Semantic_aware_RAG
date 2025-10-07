n, m, t = map(int, input().split())
A = list(map(int, input().split()))
# The original variable name was 'a', but keep consistency with the rest of the code
# Replace A with a so the rest of the code works as intended
a = A
pos = 0

for i in range(m):
    x, y = map(int, input().split())
    t -= sum(a[pos : x - 1])
    if t <= 0:
        print("No")
        exit()
    else:
        t += y
        pos = x - 1
t -= sum(a[pos:])
if t <= 0:
    print("No")
else:
    print("Yes")
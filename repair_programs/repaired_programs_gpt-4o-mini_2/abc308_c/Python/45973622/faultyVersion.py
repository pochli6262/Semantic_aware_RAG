N = int(input())
L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append(((A*10**100)/(A+B), i))
L.sort(key=lambda x: (-x[0], x[1]))
for i, j in L:
    print(j+1, end=' ')
print()
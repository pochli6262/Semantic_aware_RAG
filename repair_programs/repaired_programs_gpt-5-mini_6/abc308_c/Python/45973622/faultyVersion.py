N = int(input())
L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append((__import__('fractions').Fraction(A, A+B), -i))
L.sort(reverse=True)
for i, j in L:
    print(-j+1, end=' ')
print()

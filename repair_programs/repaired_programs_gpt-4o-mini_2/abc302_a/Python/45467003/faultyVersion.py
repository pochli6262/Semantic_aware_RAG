A, B = map(int, input().split())

if B != 0:
    print(1 + A // B)
else:
    print('Error: Division by zero')
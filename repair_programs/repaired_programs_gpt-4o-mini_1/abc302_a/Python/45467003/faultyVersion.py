A, B = map(int, input().split())

if B == 0:
    print('Error: Division by zero is not allowed')
else:
    print(1 + A // B)
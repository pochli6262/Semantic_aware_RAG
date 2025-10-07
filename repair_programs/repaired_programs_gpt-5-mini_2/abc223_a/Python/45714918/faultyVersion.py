x = int(input())
print('Yes' if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0) else 'No')
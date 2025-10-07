n = int(input())

for i in range(6):
    if n < 10**(3 + i):
        print((n // (10**i)) * 10**i)
        break
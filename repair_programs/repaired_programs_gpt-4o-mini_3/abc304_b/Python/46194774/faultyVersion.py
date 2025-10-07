N = int(input())

if N <= 10 ** 3 - 1:
    print(N)
elif 10 ** 3 <= N < 10 ** 4:
    print(N // 10 * 10)
elif 10 ** 4 <= N < 10 ** 5:
    print(N // 100 * 100)
elif 10 ** 5 <= N < 10 ** 6:
    print(N // 1000 * 1000)
elif 10 ** 6 <= N < 10 ** 7:
    print(N // 10000 * 10000)
elif 10 ** 7 <= N < 10 ** 8:
    print((N // 100000) * 100000)
else:
    None
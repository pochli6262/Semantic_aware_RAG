K = sorted(list(map(int, input().split())))

if K.count(K[0]) == 3 and K.count(K[2]) == 2:
    print('Yes')
else:
    print('No')
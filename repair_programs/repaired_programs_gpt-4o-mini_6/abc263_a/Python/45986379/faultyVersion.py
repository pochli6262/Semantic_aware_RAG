K = sorted(list(map(int, input().split())))

if (K.count(K[0]) == 3 and K.count(K[1]) == 2) or (K.count(K[0]) == 2 and K.count(K[1]) == 3):
    print('Yes')
else:
    print('No')
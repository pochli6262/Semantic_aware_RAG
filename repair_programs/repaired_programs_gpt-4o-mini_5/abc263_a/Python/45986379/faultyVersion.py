K = sorted(list(map(int, input().split())))

if len(set(K)) == 2 and K.count(K[0]) == 3:
    print('Yes')
else:
    print('No')
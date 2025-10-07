K = sorted(list(map(int, input().split())))

if len(set(K)) == 2 and K[0] != K[1]:
    print('Yes')
else:
    print('No')
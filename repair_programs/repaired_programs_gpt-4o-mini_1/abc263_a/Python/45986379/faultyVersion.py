K = sorted(list(map(int, input().split())))

if len(set(K)) == 2 and len(K) >= 4 and K[2] != K[3]:
    print('Yes')
else:
    print('No')
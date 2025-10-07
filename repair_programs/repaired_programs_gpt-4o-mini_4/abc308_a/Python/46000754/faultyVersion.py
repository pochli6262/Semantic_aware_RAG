S = list(map(int, input().split()))

N = len(S)
if sorted(S) != S or not all(100 <= s <= 675 and s % 25 == 0 for s in S):
    print('No')
    exit()
else:
    print('Yes')
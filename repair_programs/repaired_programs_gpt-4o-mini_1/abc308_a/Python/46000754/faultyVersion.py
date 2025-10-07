S = list(map(int, input().split()))

N = len(S)
if sorted(S) == S:
    print('No')
    exit()
for i in range(N):
    if not(100 <= S[i] <= 675) or S[i] % 25 != 0:
        print('No')
        exit()
else:
    print('Yes')
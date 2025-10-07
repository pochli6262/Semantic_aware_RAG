S = list(map(int, input().split()))

N = len(S)
for i in range(N):
    if not(100 <= S[i] <= 675) or S[i]%25 != 0 or sorted(S) != S:
        print('No')
        exit()
else:
    print('Yes')
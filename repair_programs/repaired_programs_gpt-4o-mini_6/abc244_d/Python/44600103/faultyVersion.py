S = list(map(str, input().split()))
T = list(map(str, input().split()))
diff = 0
for i in range(3):
    if S[i] != T[i]:
        diff += 1

if diff % 2 == 0 and S.count('R') == T.count('R') and S.count('G') == T.count('G') and S.count('B') == T.count('B'):
    print('Yes')
else:
    print('No')
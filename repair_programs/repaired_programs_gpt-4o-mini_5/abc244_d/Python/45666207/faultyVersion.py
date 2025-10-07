S = [a for a in input().split()]
T = [a for a in input().split()]

cnt = 0
for i in range(3):
    if S[i] == T[i]:
        cnt += 1

if cnt % 2 == 1 or S.count('R') != T.count('R') or S.count('G') != T.count('G') or S.count('B') != T.count('B'):
    print("No")
else:
    print("Yes")
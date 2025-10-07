S = [a for a in input().split()]
T = [a for a in input().split()]

cnt = 0
for i in range(3):
    if S[i] == T[i]:
        cnt += 1

if T == S or T == S[1:]+S[:1] or T == S[2:]+S[:2]:
    print("Yes")
else:
    print("No")
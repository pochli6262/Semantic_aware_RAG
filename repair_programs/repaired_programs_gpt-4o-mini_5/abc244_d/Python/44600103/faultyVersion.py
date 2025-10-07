S = list(map(str, input().split()))
T = list(map(str, input().split()))
diff = 0
for i in range(3):
    if S[i] != T[i]:
        diff += 1

if sorted(S) == sorted(T):
    print('Yes')
else:
    print('No')
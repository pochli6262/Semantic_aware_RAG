S = list(map(str, input().split()[:3]))
T = list(map(str, input().split()[:3]))
diff = 0
for i in range(3):
    if S[i] != T[i]:
        diff += 1

if diff % 2 == 0:
    print('Yes')
else:
    print('No')
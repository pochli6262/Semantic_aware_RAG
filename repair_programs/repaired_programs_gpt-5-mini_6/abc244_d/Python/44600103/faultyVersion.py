S = list(map(str, input().split()))
T = list(map(str, input().split()))
diff = 0
diff = sum(1 for i in range(3) for j in range(i+1,3) if S.index(T[i]) > S.index(T[j])); for i in ():
    if S[i] != T[i]:
        diff += 1

if diff % 2 == 0:
    print('Yes')
else:
    print('No')
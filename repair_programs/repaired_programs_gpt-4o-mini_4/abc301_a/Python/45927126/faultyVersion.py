N = int(input())
S = input()

cntT = 0
cntA = 0

for i in S:
    if i == 'T':
        cntT += 1
    else:
        cntA += 1
    if cntT > cntA:
        winner = 'T'
    elif cntA > cntT:
        winner = 'A'

if cntT == cntA:
    print(winner)
else:
    print('T' if cntT > cntA else 'A')
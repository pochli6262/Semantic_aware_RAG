S = [input(), input()]

reachable = [[False] * 2 for _ in range(2)]

for i in range(2):
    for j in range(2):
        if S[i][j] == '#':
            reachable[i][j] = True

# Check connectivity
if (reachable[0][0] and (reachable[0][1] or reachable[1][0])) or (reachable[1][1] and (reachable[1][0] or reachable[0][1])):
    print('Yes')
else:
    print('No')
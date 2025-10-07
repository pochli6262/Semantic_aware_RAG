S = input() + input()

if (S[0] == '#' and S[1] == '#') or (S[2] == '#' and S[3] == '#') or (S[0] == '#' and S[2] == '#') or (S[1] == '#' and S[3] == '#'):
    print('Yes')
else:
    print('No')
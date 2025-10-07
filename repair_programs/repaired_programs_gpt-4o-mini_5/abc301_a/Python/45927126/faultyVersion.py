N = int(input())
S = input()

t_score = 0
 a_score = 0

for i in S:
    if i == 'T':
        t_score += 1
    else:
        a_score += 1

if t_score > a_score:
    print('T')
elif a_score > t_score:
    print('A')
else:
    print('T' if S.index('T') < S.index('A') else 'A')
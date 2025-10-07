list_A_B = list(map(int, input().split()));
A = list_A_B[0]
B = list_A_B[1]

if B-A == 1 or A-B == 9:
    print('Yes')
else:
    print('No')
G = [[1, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9], [1, 4], [4, 7], [2, 5], [5, 8], [3, 6], [6, 9]]

R = list(map(int, input().split()))

flag = False
for g in G:
    if abs(R[0] - R[1]) == 1:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
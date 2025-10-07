n = int(input())
a = []
for _ in range(n):
    cur_a = list(map(int, input().split()))
    a.append(cur_a)
b = []
for _ in range(n):
    cur_b = list(map(int, input().split()))
    b.append(cur_b)

import numpy as np
for i in range(1,4):
    a90 = np.rot90(a, k = -i)
    ans = True
    for j in range(n):
        for k in range(n):
            if a90[j][k] == 1:
                if b[j][k] != 1:
                    ans = False
                    break  # Corrected line: break upon mismatch
        if not ans:
            break  # Additional break to exit outer loop on failure
    if ans:
        break   
if ans:
    print("Yes")
else:
    print("No")
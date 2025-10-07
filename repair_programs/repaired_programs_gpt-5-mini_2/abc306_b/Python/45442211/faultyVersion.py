A = list(map(int,input().split()))
S = 0

import math

for i in range(len(A)):
    S = S + A[i]*(pow(2,i))
    
print(S)
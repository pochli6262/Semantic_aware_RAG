# Copyright (c) 2023, Le Duc Phuc Long

# If you don't think twice, you have to code twice.

# Import session
import sys
#input = sys.stdin.readline
from collections import defaultdict

############ ---- Input Functions ---- ############
def inp():
    return int(input())

def inlt():
    return list(map(int, input().split()))

def instr():
    return list(input().strip())

def invr():
    return map(int, input().split())

############ ---- Other Functions ---- ############
# Precompute

# IO
#input = sys.stdin.readline
# sys.stdin = open('in.txt', 'r')
# sys.stdout = open('out.txt', 'w')
# Main function
n, m = invr()
mtx = [list(input()) for _ in range(n)]


ans = [0]*(n+1)
for i in range(n):
    for j in range(m):
        # Check for crosses explicitly
        if mtx[i][j] == '#':
            size = 0
            can_increment = True
            while can_increment:
                size += 1
                for d in range(1, size + 1):
                    if (i+d < n and j+d < m and mtx[i+d][j+d] == '#' and 
                        i+d < n and j-d >= 0 and mtx[i+d][j-d] == '#' and 
                        i-d >= 0 and j+d < m and mtx[i-d][j+d] == '#' and 
                        i-d >= 0 and j-d >= 0 and mtx[i-d][j-d] == '#'):
                        continue
                    else:
                        can_increment = False
                        break
            if size > 0:
                ans[size] += 1

ans.pop(0)

print(' '.join(map(str, ans)))
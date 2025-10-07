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

def dfs(x, y, size):
    if size < 1:
        return 0
    # Check the current cross size
    valid = True
    for d in range(size + 1):
        if mtx[x+d][y+d] != '#' or mtx[x+d][y-d] != '#' or \
           mtx[x-d][y+d] != '#' or mtx[x-d][y-d] != '#':
            valid = False
            break
    if valid:
        # Check for the existence of at least one ending condition
        if (0 <= x+size+1 < n and 0 <= y+size+1 < m and mtx[x+size+1][y+size+1] == '.') or \
           (0 <= x+size+1 < n and 0 <= y-size-1 < m and mtx[x+size+1][y-size-1] == '.') or \
           (0 <= x-size-1 < n and 0 <= y+size+1 < m and mtx[x-size-1][y+size+1] == '.') or \
           (0 <= x-size-1 < n and 0 <= y-size-1 < m and mtx[x-size-1][y-size-1] == '.'):
            return 1 + dfs(x, y, size + 1)
    return 0

ans = [0]*(n+1)
for i in range(n):
    for j in range(m):
        if mtx[i][j] == '#':
            size = dfs(i, j, 1)
            ans[size] += 1

ans.pop(0)

print(' '.join(map(str, ans)))
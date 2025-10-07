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
        if mtx[i][j] == '#':
            d = 0
            is_cross = True
            while is_cross:
                d += 1
                # Check current size d cross
                if not (0 <= i+d < n and 0 <= j+d < m and 0 <= j-d < m and 0 <= i-d < n):
                    is_cross = False
                    break
                if mtx[i][j] != '#' or mtx[i+d][j+d] != '#' or mtx[i+d][j-d] != '#' or mtx[i-d][j+d] != '#' or mtx[i-d][j-d] != '#':
                    is_cross = False
                    break
                # Check if the outer positions are valid
                if (i + d + 1 < n and (mtx[i + d + 1][j + d + 1] != '#') and (mtx[i + d + 1][j - d - 1] != '#') and (mtx[i - d - 1][j + d + 1] != '#') and (mtx[i - d - 1][j - d - 1] != '#')):
                    ans[d] += 1
                else:
                    is_cross = False
                # Mark the current cross as counted
                mtx[i][j] = '.'
                mtx[i+d][j+d] = '.'
                mtx[i+d][j-d] = '.'
                mtx[i-d][j+d] = '.'
                mtx[i-d][j-d] = '.'

ans.pop(0)

print(' '.join(map(str, ans)))
import sys
sys.setrecursionlimit(10 ** 5 + 10000)
input = sys.stdin.readline

def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LIS(): return list(map(int, SI()))
def LA(f): return list(map(f, input().split()))
def LLI(H): return [LI() for _ in range(H)]
INF = float('inf')
import decimal
from decimal import Decimal
import math
from math import ceil, floor, log2, log, sqrt, gcd
def lcm(x, y): return (x * y) // gcd(x, y)
from itertools import combinations as comb, combinations_with_replacement as comb_w, product, permutations, accumulate
from collections import deque, defaultdict
from pprint import pprint
import operator
from copy import deepcopy
MOD = 10**9+7
MOD2 = 998244353
def y(): print('Yes'); exit()
def n(): print('No'); exit()
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

def solve():
    ans = INF

    n,m,t = MI()
    A = LI()
    L = LLI(m)

    d = defaultdict(int)
    for x, y in L:
        d[x] = y

    for i, a in enumerate(A):
        room = i          # Changed room from i + 1 to i
        if d[room]:
            t += d[room]
        t -= a
        if t >= 0:
            continue
        else:
            print("No")
            exit()
    
    print("Yes")


if __name__ == '__main__':
    solve()
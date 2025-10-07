# Python3/Pypy3テンプレート集

#ライブラリ-------------------------------------------------------------------
from bisect import *
import heapq
import collections
from collections import deque
from queue import Queue
from itertools import groupby
import itertools
import math
import array
import string
import copy
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from functools import reduce
from operator import and_, or_, xor

#便利スクリプト---------------------------------------------------------------
INF = 10**20
mod = 998244353
MOD = 10**9+7
def YesNo(b): print("Yes") if b else print("No")
def YESNO(b): print("YES") if b else print("NO")

#標準入力---------------------------------------------------------------------
import sys
sys.setrecursionlimit(10 ** 5 + 10000)
input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LIS(): return list(map(str, SI()))
def LA(f): return list(map(f, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return input().strip('\n')
def MS(): return input().split()
def LS(): return list(input().strip('\n'))
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def LMS(rows_number): return [MS() for _ in range(rows_number)]

#関数------------------------------------------------------------------------
###標準ライブラリ###
def ceil(a,b): #切り捨て
    return (a+b-1)//b

def inv(a,p): #aのpを法とする逆元(aとpは互いに素)
    return pow(a,p-2,p)%p

def transpose(A): #二次元配列の転置
    A_t = []
    for i in range(len(A[0])) :
        tmp = []
        for v in A :
            tmp.append(v[i])
        A_t.append(tmp)
    return A_t

#... (rest of the unchanged code)

N, D = MI()
A = LLI(N)

def isVirus(X1,Y1,X2,Y2):
    return ((X1-X2)**2 + (Y1-Y2)**2)**(1/2) <= D

uf = UnionFind(N)

for i in range(N):
    for j in range(N):
        if(isVirus(A[i][0],A[i][1],A[j][0],A[j][1])):
            uf.union(i,j)
            
dict = uf.all_group_members()

for i in range(N):
    if i in dict[uf.find(0)]:
        print('Yes')
    else:
        print('No')
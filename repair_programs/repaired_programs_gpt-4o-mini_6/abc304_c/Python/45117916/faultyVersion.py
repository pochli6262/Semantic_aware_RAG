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
def LIS(): return list(map(int, SI()))
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

def rotate_matrix(A): #グリッドを時計回りに90度回転
    return transpose(A[::-1])

def removeDuplicates_2D(A): #二次元配列の重複削除
    return list(map(list, set(map(tuple, A))))

def convert(S,c): # グリッドをの 黒 マスの点集合に変換する | S: グリッド c:黒マスがなにか(ex #,1)
    s = set()
    h = len(S)
    w = len(S[0])
    for i in range(h):
        for j in range(w):
            if S[i][j] == c:
                s.add((i, j))
    return s

def normalize(s): # グリッドの # マスの点集合を与えると最小の x 座標と最小の y 座標がともに 0 となるように平行移動して返す
    mi = min(i for (i, j) in s)
    mj = min(j for (i, j) in s)
    return set((i - mi, j - mj) for (i, j) in s)

def cumulativeSum_1D(A): #配列Aの累積和
  return list(itertools.accumulate(A))

...  # (other utility functions remain unchanged)

###デバッグ用ライブラリ###
def TS(_str): #変数/リストに格納されている値を確認
    print('{}: {}'.format(_str, eval(_str)))

def T2d(A): #二次元配列の確認用
    for a in A:
        print(*a)

#クラス----------------------------------------------------------------------
from collections import defaultdict 
 
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
 
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#カンニングペーパー-----------------------------------------------------------
# ... (other comments and instructions remain unchanged)

#PyPyで再帰関数を用いる場合はコメントを外す----------------------------------
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

#----------------------------------------------------------------------------
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
    if uf.same(0, i):  # FIXED LINE
        print('Yes')
    else:
        print('No')
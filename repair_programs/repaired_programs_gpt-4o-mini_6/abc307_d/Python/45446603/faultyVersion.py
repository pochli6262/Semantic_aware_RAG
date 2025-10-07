#再帰はCpython,その他はpypy
import sys
sys.setrecursionlimit(1000000)
from collections import deque
from collections import defaultdict

n = int(input())
s = str(input())
s = list(s)

sakuzyo = deque([])
ans = []

for i,mozi in enumerate(s):
    #print(sakuzyo)
    if mozi == "(":
        sakuzyo.append(i)
        ans.append(mozi)

    elif mozi == ")":
        if sakuzyo:
            ans = ans[:sakuzyo.pop()] + ans[sakuzyo[-1]+1:]  # this line is fixed
        else:
            ans.append(mozi)
    else:
        ans.append(mozi)

print("".join(ans))
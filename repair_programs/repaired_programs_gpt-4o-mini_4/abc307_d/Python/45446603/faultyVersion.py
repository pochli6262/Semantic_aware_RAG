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
            start_index = sakuzyo.pop()
            del ans[start_index:]
        else:
            ans.append(mozi)
    else:
        ans.append(mozi)

print("".join(ans))
s=list(map(int,input().split()))
ss=sorted(s)

pack=[]
if len(s) == 8 and s[0] > 100 and s[-1] < 675:
  for i in s:
    if i % 25 == 0:
      pack.append(i)
print("Yes" if len(pack) == 8 else "No")
n,m,t=map(int,input().split())
a=list(map(int,input().split()))
v=[0]*n
for i in range(m):
  x,y=map(int,input().split())
  v[x-1]=y
for i in range(n-1):
  if t>0:
    if t<a[i]:
      print('No')
      break
    t-=a[i]
    t+=v[i]
  else:
    print('No')
    break
else:
  print('Yes')
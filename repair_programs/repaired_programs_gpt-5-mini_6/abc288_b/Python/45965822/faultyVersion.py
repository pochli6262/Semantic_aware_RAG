a,b=map(int,input().split())
c=[]
for i in range(a):
    c.append(str(input()))
c=c[:b]; c.sort()
c=c[0:b]
for i in c:
  print(i)
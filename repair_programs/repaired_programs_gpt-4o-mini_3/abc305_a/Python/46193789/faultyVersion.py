N=int(input())
values=[]
for i in range(20):
  values.append(abs(N-i*5))
In=values.index(min(values))
print(In*5)
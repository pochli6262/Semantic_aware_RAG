N=int(input())
list=[]
for i in range(20):
  list.append(abs(N-i*5))
index=list.index(min(list))
print(index*5)
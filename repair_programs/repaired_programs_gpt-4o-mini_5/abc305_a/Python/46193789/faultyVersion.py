N=int(input())
list=[]
for i in range(21):
  list.append(abs(N-i*5))
In=list.index(min(list))
closest_station = In * 5
print(closest_station)
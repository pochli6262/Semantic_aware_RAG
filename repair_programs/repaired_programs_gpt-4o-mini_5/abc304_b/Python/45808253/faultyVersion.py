N = int(input())
key = N
point = 0
l = []
while  key > 0:
    s = key % 10
    key = key // 10
    point += 1
    l.append(s)

if point <= 3:
    print(N)
elif point == 4:
    l[0] = 0
    for i in range(point-1, -1, -1):
        print(l[i],end='')
elif point >= 5:
    l[0:point-1] = [0]*(point-1)
    for i in range(point-1, -1, -1):
        print(l[i],end='')
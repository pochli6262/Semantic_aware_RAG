n = int(input())
a = list(map(int, input().split()))
b = []
i_bef = 0
for i in a:
    if i_bef == 0: 
        b.append(i)
        i_bef = i
        continue
    dif = i - i_bef
    if abs(dif) > 1:
        if dif > 0:
            for j in range(1, abs(dif)):
                b.append(i_bef + j)
            b.append(i)
        else:
            for j in range(1, abs(dif)):
                b.append(i_bef - j)
            b.append(i)
    else:
        b.append(i)
    i_bef = i
print(*b)
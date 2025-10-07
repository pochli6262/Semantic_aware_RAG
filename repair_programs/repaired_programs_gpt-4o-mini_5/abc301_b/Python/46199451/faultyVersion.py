n = int(input())
a = list(map(int, input().split()))

ans_list = []
for i in range(n - 1):
    if a[i + 1] > a[i]:
        ans_list.extend(j for j in range(a[i] + 1, a[i + 1]))
    elif a[i + 1] < a[i]:
        ans_list.extend(j for j in range(a[i] - 1, a[i + 1], -1))
ans_list.append(a[-1])
print(ans_list)
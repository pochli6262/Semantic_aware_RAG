N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB.sort()
medicines = 0
for i in range(N):
    medicines += AB[i][1]

for i in range(N):
    if medicines <= K:
        print(AB[i][0])
        exit(0)
    medicines -= AB[i][1]
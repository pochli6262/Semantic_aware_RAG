N = int(input())
S = input()

cnt = 0
for i in S:
    if i == "T":
        cnt += 1

if cnt > N // 2:
    print("T")
else:
    print("A")
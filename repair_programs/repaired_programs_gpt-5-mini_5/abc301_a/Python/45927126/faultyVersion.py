N = int(input())
S = input()

cnt = 0
for i in S:
    if i == "T":
        cnt += 1

if cnt > N - cnt:
    print("T")
else:
    if cnt < N - cnt:
        print("A")
    else:
        t = a = 0
        target = cnt
        for ch in S:
            if ch == "T":
                t += 1
            else:
                a += 1
            if t == target:
                print("T")
                break
            if a == target:
                print("A")
                break
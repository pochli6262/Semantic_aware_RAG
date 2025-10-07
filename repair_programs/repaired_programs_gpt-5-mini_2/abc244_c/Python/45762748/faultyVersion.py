N=int(input())
bad=set()
for _ in range(N):
    for i in range(1,N+1):
        if i not in bad:
            bad.add(i)
            print(i)
            bad.add(int(input()))
            break

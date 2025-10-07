N=int(input())
bad=set()
while len(bad) < N:
    for i in range(1,N+1):
        if i not in bad:
            bad.add(i)
            print(i)
            bad.add(int(input()))
            break

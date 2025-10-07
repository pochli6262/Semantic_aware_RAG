N=int(input())
a=N%5   

if a==0:
    print(N)
else:
    if a < 3:
        ans=N-a
    else:
        ans=N+a
    # Determine the nearest water station correctly
    if ans % 5 != 0:
        if (N - (N // 5) * 5) < ((N // 5 + 1) * 5 - N):
            ans = (N // 5) * 5
        else:
            ans = (N // 5 + 1) * 5
    print(ans)
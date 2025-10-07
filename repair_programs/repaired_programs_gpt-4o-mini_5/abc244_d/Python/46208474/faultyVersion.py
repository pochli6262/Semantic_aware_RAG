S=list(input().split())
T=list(input().split())

if sorted(S) == sorted(T):
    print("Yes")
else:
    print("No")
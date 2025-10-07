S=input()
T=input()
A=["R G B","B R G","G B R"]
if sorted(S.split()) == sorted(T.split()):
    print("Yes")
else:
    print("No")
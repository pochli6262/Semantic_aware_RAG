S=list(map(int,input().split()))
check_S=sorted(S)
check="True"
check_num=0
for i in range (len(S)):
    if check_num<check_S[i] and 100<=check_S[i]<=675 and check_S[i]%25==0:
        check_num=check_S[i]
    else:
        check="False"
if check=="True":
    print("Yes")
else:
    print("No")
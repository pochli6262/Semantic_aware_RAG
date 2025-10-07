S=list(map(int,input().split()))
check="True"
check_num=0
for i in range (len(S)):
    if (i == 0 or S[i] >= S[i-1]) and 100<=S[i]<=675 and S[i]%25==0:
        check_num=S[i]
    else:
        check="False"
if check=="True":
    print("Yes")
else:
    print("No")
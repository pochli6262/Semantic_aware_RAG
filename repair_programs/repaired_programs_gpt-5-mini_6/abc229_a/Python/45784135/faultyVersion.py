s1=input()
s2=input()

if not ((s1[0]=="#" and s2[1]=="#" and s1[1]=="." and s2[0]==".") or (s1[1]=="#" and s2[0]=="#" and s1[0]=="." and s2[1]==".")):
    print("Yes")
else:
    print("No")
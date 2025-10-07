S1 = input()
S2 = input()
if not ((S1+S2).count('#')==2 and ((S1[0]=='#' and S2[1]=='#') or (S1[1]=='#' and S2[0]=='#'))):
    print("Yes")
else:
    print("No")
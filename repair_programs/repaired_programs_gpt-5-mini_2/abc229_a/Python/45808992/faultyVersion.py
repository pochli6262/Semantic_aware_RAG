S1 = input()
S2 = input()
if S1 == "##" or S2 == "##" or (S1[0] == "#" and S2[0] == "#") or (S1[1] == "#" and S2[1] == "#"):
    print("Yes")
elif S1 == ".#" and S2 == "#.":
    print("No")
elif S1 == "#." and S2 == ".#":
    print("No")
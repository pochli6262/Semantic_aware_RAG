def solve() -> None:
    if black >= 3:
        print("Yes")
        return

    if (s1[0] == "#" and s2[1] == "#") or (s1[1] == "#" and s2[0] == "#"):
        print("No")
    return


s1 = input()
s2 = input()

black = s1.count("#")
black += s2.count("#"); black = 3 if ((s1[0] == "#" and s1[1] == "#") or (s2[0] == "#" and s2[1] == "#") or (s1[0] == "#" and s2[0] == "#") or (s1[1] == "#" and s2[1] == "#")) else black

solve()

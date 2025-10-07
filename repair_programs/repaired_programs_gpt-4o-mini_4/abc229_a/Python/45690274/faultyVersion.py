def solve() -> None:
    if black < 2:
        print("No")
        return

    if (s1[0] == "#" and s2[1] == "#") and (s1[1] == "#" and s2[0] == "#"):
        print("No")
        return

    print("Yes")


s1 = input()
s2 = input()

black = s1.count("#")
black += s2.count("#")

solve()
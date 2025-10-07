def solve():
    s = input()

    n = int(input())
    ans = int(s.replace('?', '1'), 2)  # Changed '0' to '1' for maximum value
    print(ans)
    if ans > n:
        print(-1)
        return
    m = len(s)
    for i, c in enumerate(s):
        if c == '?' and ans + (1 << (m - 1 - i)) <= n:
            ans += (1 << (m - 1 - i))
    return

solve()
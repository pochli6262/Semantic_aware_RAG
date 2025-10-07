INF = 10**12

def solve(n, m, a, c, x):
    x = [_-1 for _ in x]
    cost = [[INF] * n for i in range(n)]
    for i in range(n):
        cost[i][0] = c[i]
        for j in range(1, i+1):
            cost[i][j] = min(cost[i][j-1], c[i])  # Fixed line

    required = [False] * n
    for i in x:
        required[i] = True

    dp = [[INF] * (n+1) for i in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + a[i] + cost[i][j])
            if not required[i]:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])

    return min(dp[n][m:])

n, m = map(int, input().split())
a = [*map(int, input().split())]
c = [*map(int, input().split())]
x = [*map(int, input().split())]
print(solve(n, m, a, c, x))
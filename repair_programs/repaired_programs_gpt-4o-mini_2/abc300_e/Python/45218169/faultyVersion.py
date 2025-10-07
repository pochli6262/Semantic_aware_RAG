def ezpow(a, b):
    c = 1
    for i in range(b):
        c = c * a
    return c

class PowMod:
    def __init__(self, A, m=998244353):
        self.memory = {}
        self.A = A
        self.m = m
    def pow(self, b):
        if (b == 0):
            return 1
        if (b == 1):
            return self.A
        if (b in self.memory):
            return self.memory[b]
        m = self.m
        bdiv2 = b//2
        lf = self.pow(bdiv2)
        rg = self.pow(b-bdiv2)
        self.memory[b] = ((lf % m) * (rg % m)) % m
        return ((lf % m) * (rg % m)) % m

def reciprocalMod(a, p=998244353):
    powMod = PowMod(a, p)
    return powMod.pow(p-2)

N = int(input())

curN = N
factors = {2: 0, 3: 0, 5: 0}
while (True):
    if (curN == 1):
        break
    divided = False
    for p in [2, 3, 5]:
        if (curN % p == 0):
            curN //= p
            factors[p] += 1
            divided = True
            break
    if (not divided):
        print(0)
        exit()
        
X = factors[2]
Y = factors[3]
Z = factors[5]

BIGPRIME = 998244353
recip5 = reciprocalMod(5, BIGPRIME)
order = []
for x in range(X+1):
    for y in range(Y+1):
        for z in range(Z+1):
            order.append((ezpow(2, x) * ezpow(3, y) * ezpow(5, z), x, y, z))
order.sort()            
dp = [[[0 for _ in range(Z+1)] for _ in range(Y+1)] for _ in range(X+1)]
dp[0][0][0] = 1

for num, x, y, z in order:
    if (x + 1 <= X): # 2
        dp[x+1][y][z] += (dp[x][y][z] * recip5) % BIGPRIME
        if (x + 2 <= X): # 4
            dp[x+2][y][z] += (dp[x][y][z] * recip5) % BIGPRIME
        if (x + 1 <= X and y + 1 <= Y): # 6
            dp[x+1][y+1][z] += (dp[x][y][z] * recip5) % BIGPRIME
    if (y + 1 <= Y): # 3
        dp[x][y+1][z] += (dp[x][y][z] * recip5) % BIGPRIME
    if (z + 1 <= Z): # 5
        dp[x][y][z+1] += (dp[x][y][z] * recip5) % BIGPRIME

print(dp[X][Y][Z] % BIGPRIME)
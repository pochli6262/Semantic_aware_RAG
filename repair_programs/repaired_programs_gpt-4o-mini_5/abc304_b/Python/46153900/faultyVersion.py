N = int(input())

print(round(N, -1 if N < 10**3 else
      1 if 10**3 <= N < 10**4 else
      2 if 10**4 <= N < 10**5 else
      3 if 10**5 <= N < 10**6 else
      4 if 10**6 <= N < 10**7 else
      5 if 10**7 <= N < 10**8 else
      6))
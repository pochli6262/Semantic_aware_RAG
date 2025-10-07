n = int(input())
s = list(map(int,input().split()))

for i in range(n - 6):  # Adjust index to prevent exceeding the length of 's'
  ans = 0
  for l in range(7):
    ans += s[l + i]  # Corrected to safely access elements

  print(str(ans), "", end="")
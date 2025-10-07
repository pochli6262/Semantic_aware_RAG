N = int(input())
S = input()
t, a = 0, 0
for i in range(N):
  if S[i] == "T":
    t += 1
  else:
    a += 1
  if t > a:
    print("T")
    break
  elif a > t:
    print("A")
    break
if t == a:
  print("T" if S.rfind('T') < S.rfind('A') else "A")
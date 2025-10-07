N = int(input())
S = input()
t, a, t_win, a_win = 0, 0, False, False
for i in range(N):
  if S[i] == "T":
    t += 1
  else:
    a += 1
  if t > a:
    t_win = True
  elif a > t:
    a_win = True
if t > a:
  print("T")
elif a > t:
  print("A")
else:
  if t_win:
    print("T")
  else:
    print("A")
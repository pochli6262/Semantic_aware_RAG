N = int(input())
S = input()
t, a, t_win, a_win = 0, 0, False, False
for i in range(N):
  if S[i] == "T":
    t += 1
  else:
    a += 1
  if N % 2 == 0 and t == a:
    t_win, a_win = True, True
if t > a:
  t_win = True
elif a > t:
  a_win = True
if t_win == True:
  print("T")
if a_win == True:
  print("A")
s = input()
t = input()
cnt = 0
for i in range(3):
    if s[i] != t[i]:
        cnt += 1
if cnt == 0:
    print("Yes")
elif cnt == 3:
    print("Yes")  # changing this line to always print Yes if all hats are different
else:
    print("No")
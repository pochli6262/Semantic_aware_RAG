arr = list(map(int, input().split()))
fl = True
for i in range(1, 8):
    if arr[i - 1] > arr[i]:
        fl = False
if any(s % 25 != 0 for s in arr):
    fl = False
print("Yes" if fl else "No")
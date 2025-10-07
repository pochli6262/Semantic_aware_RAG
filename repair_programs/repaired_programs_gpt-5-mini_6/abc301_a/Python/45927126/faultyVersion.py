N = int(input())
S = input()

cnt = 0
for i in S:
    if i == "T":
        cnt += 1

if cnt > N - cnt:
    print("T")
else:
    print("A" if cnt < N - cnt else ("T" if [i for i,c in enumerate(S) if c=='T'][cnt-1] < [i for i,c in enumerate(S) if c=='A'][cnt-1] else "A"))
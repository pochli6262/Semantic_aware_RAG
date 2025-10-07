N = int(input())
S = input()

cnt = 0
for i in S:
    if i == "T":
        cnt += 1

if cnt > N - cnt:
    print("T")
elif cnt < N - cnt:
    print("A")
else:
    # Determine who reached the wins first
    t_wins = 0
    a_wins = 0
    for i in range(N):
        if S[i] == 'T':
            t_wins += 1
        else:
            a_wins += 1
        if t_wins > a_wins:
            print("T")
            break
        elif a_wins > t_wins:
            print("A")
            break
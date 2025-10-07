x = list(map(int, input().split()))
cards_count = {n: x.count(n) for n in set(x)}
if sorted(cards_count.values()) == [2, 3]:
    print("Yes")
else:
    print("No")
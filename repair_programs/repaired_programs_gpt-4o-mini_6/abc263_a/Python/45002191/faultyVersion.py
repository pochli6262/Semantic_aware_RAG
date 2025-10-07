x=list(map(int,input().split()))
from collections import Counter
counts = Counter(x)
if sorted(counts.values()) == [2, 3]:
    print("Yes")
else:
    print("No")
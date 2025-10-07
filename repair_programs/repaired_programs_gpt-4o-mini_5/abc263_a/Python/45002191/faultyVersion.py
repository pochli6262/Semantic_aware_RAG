x=list(map(int,input().split()))
from collections import Counter
counts = Counter(x).values()
if sorted(counts) == [2, 3]:
    print("Yes")
else:
    print("No")
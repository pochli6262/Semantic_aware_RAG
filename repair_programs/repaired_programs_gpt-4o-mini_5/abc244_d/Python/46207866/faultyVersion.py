S1,S2,S3 = input().split()
T1,T2,T3 = input().split()

# Count occurrences of each hat color
from collections import Counter
S_count = Counter([S1, S2, S3])
T_count = Counter([T1, T2, T3])

# Check if the counts of each hat type are the same
if S_count == T_count:
    print('Yes')
else:
    print('No')
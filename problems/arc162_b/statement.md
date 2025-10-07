Score : 500 points

### Problem Statement

A permutation P=(P\_1,P\_2,\ldots,P\_N) of (1,2,\ldots,N) is given.

Determine whether it is possible to rearrange P in ascending order by performing the following operation at most 2\times 10^3 times, and if possible, show one such sequence of operations.

* Choose integers i and j such that 1\leq i \leq N-1,0 \leq j \leq N-2. Let Q = (Q\_1, Q\_2,\ldots,Q\_{N-2}) be the sequence obtained by removing (P\_i,P\_{i+1}) from P. Replace P with (Q\_1,\ldots,Q\_j, P\_i, P\_{i+1}, Q\_{j+1},\ldots,Q\_{N-2}).

### Constraints

* 2 \leq N \leq 10^3
* P is a permutation of (1,2,\ldots,N).
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
P_1 P_2 \ldots P_N
```

### Output

If P cannot be rearranged in ascending order within 2\times 10^3 operations, print `No`. If it can be rearranged in ascending order, let M\ (0 \leq M \leq 2\times 10^3) be the number of operations, and i\_k,j\_k be the chosen i,j for the k-th operation (1\leq k \leq M), and print them in the following format:

```
Yes
M
i_1 j_1
i_2 j_2
\vdots
i_M j_M
```

If there are multiple solutions, any of them will be considered correct.

---

### Sample Input 1

```
5
1 4 2 3 5
```

### Sample Output 1

```
Yes
1
3 1
```

Perform the operation with i=3,j=1.

Then, Q=(P\_1,P\_2,P\_5)=(1,4,5), so you get P=(Q\_1,P\_3,P\_4,Q\_2,Q\_3) = (1,2,3,4,5).

Thus, P can be rearranged in ascending order with one operation.

---

### Sample Input 2

```
2
2 1
```

### Sample Output 2

```
No
```

It can be proved that P cannot be rearranged in ascending order within 2\times 10^3 operations.

---

### Sample Input 3

```
4
3 4 1 2
```

### Sample Output 3

```
Yes
3
3 0
1 2
3 0
```

There is no need to minimize the number of operations.
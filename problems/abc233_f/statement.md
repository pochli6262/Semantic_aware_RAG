Score : 500 points

### Problem Statement

We have a permutation P=(P\_1,P\_2,\ldots,P\_N) of (1,2,\ldots,N).

There are M kinds of operations available to you. Operation i swaps the a\_i-th and b\_i-th elements of P.

Is it possible to sort P in ascending order by doing at most 5\times 10^5 operations in total in any order?

If it is possible, give one such sequence of operations. Otherwise, report so.

### Constraints

* 2\leq N \leq 1000
* P is a permutation of (1,2,\ldots,N).
* 1\leq M \leq \min(2\times 10^5, \frac{N(N-1)}{2})
* 1\leq a\_i \lt b\_i\leq N
* (a\_i,b\_i)\neq (a\_j,b\_j) if i\neq j.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
P_1 P_2 \ldots P_N
M
a_1 b_1
a_2 b_2
\vdots
a_M b_M
```

### Output

If it is possible to sort P in ascending order, print the following:

```
K
c_1 c_2 \ldots c_K
```

Here, K represents the number of operations to do, and c\_i (1\leq i \leq K) means the i-th operation to do is Operation c\_i.  
Note that 0\leq K \leq 5\times 10^5 must hold.

If it is impossible to sort P in ascending order, print `-1`.

---

### Sample Input 1

```
6
5 3 2 4 6 1
4
1 5
5 6
1 2
2 3
```

### Sample Output 1

```
3
4 2 1
```

P changes as follows: (5,3,2,4,6,1)\to (5,2,3,4,6,1)\to (5,2,3,4,1,6)\to (1,2,3,4,5,6).

---

### Sample Input 2

```
5
3 4 1 2 5
2
1 3
2 5
```

### Sample Output 2

```
-1
```

We cannot sort P in ascending order.

---

### Sample Input 3

```
4
1 2 3 4
6
1 2
1 3
1 4
2 3
2 4
3 4
```

### Sample Output 3

```
0

```

P may already be sorted in ascending order.

Additionally, here is another accepted output:

```
4
5 5 5 5
```

Note that it is not required to minimize the number of operations.
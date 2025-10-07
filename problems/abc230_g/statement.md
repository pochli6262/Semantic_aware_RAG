Score : 600 points

### Problem Statement

Given is a permutation P=(P\_1,P\_2,\ldots,P\_N) of the integers from 1 through N.

Find the number of pairs of integers (i,j) such that 1\leq i\leq j\leq N satisfying GCD(i,j)\neq 1 and GCD(P\_i,P\_j)\neq 1.  
Here, for positive integers x and y, GCD(x,y) denotes the greatest common divisor of x and y.

### Constraints

* 1 \leq N \leq 2\times 10^5
* (P\_1,P\_2,\ldots,P\_N) is a permutation of (1,2,\ldots,N).
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
P_1 P_2 \ldots P_N
```

### Output

Print the answer.

---

### Sample Input 1

```
6
5 1 3 2 4 6
```

### Sample Output 1

```
6
```

Six pairs (3,3), (3,6), (4,4), (4,6), (5,5), (6,6) satisfy the condition, so 6 should be printed.

---

### Sample Input 2

```
12
1 2 3 4 5 6 7 8 9 10 11 12
```

### Sample Output 2

```
32
```
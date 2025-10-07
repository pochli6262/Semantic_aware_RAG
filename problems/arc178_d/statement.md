Score : 700 points

### Problem Statement

You are given a positive integer N and a sequence of M non-negative integers A = (A\_{1}, A\_{2}, \dots, A\_{M}).

Here, all elements of A are distinct integers between 0 and N-1, inclusive.

Find the number, modulo 998244353, of permutations P of (0, 1, \dots, N-1) that satisfy the following condition.

* After initializing a sequence B = (B\_{1}, B\_{2}, \dots, B\_{N}) to P, it is possible to make B = A by repeating the following operation some number of times:
  + Choose l and r such that 1 \leq l \leq r \leq |B|, and if \mathrm{mex}(\{B\_{l}, B\_{l+1}, \dots, B\_{r}\}) is contained in B, remove it from B.

  What is \mathrm{mex}(X)?  For a finite set X of non-negative integers, \mathrm{mex}(X) is defined as the smallest non-negative integer that is not in X.

### Constraints

* 1 \leq M \leq N \leq 500
* 0 \leq A\_{i} < N
* All elements of A are distinct.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_{1} A_{2} \cdots A_{M}
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2
1 3
```

### Sample Output 1

```
8
```

After initializing B = (2, 1, 0, 3), it is possible to make B = A using the following steps:

* Choose (l, r) = (2, 4), remove \mathrm{mex}(\{1, 0, 3\}) = 2 from B, making B = (1, 0, 3).
* Choose (l, r) = (3, 3), remove \mathrm{mex}(\{3\}) = 0 from B, making B = (1, 3).

Thus, P = (2, 1, 0, 3) satisfies the condition.

There are eight permutations P that satisfy the condition, including the above, so print 8.

---

### Sample Input 2

```
4 4
0 3 2 1
```

### Sample Output 2

```
1
```

Only P = (0, 3, 2, 1) satisfies the condition.

---

### Sample Input 3

```
16 7
9 2 4 0 1 6 7
```

### Sample Output 3

```
3520
```

---

### Sample Input 4

```
92 4
1 67 16 7
```

### Sample Output 4

```
726870122
```

Find the count modulo 998244353.
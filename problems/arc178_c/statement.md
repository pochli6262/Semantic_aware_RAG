Score : 600 points

### Problem Statement

You are given positive integers N and L, and a sequence of positive integers A = (A\_{1}, A\_{2}, \dots , A\_{N}) of length N.

For each i = 1, 2, \dots , N, answer the following question:

> Determine if there exists a sequence of L non-negative integers B = (B\_{1}, B\_{2}, \dots, B\_{L}) such that \displaystyle \sum\_{j = 1} ^ {L - 1} \sum\_{k = j + 1} ^ {L} |B\_{j} - B\_{k}| = A\_{i}. If it exists, find the minimum value of \max(B) for such a sequence B.

### Constraints

* 1 \leq N \leq 2 \times 10^{5}
* 2 \leq L \leq 2 \times 10^{5}
* 1 \leq A\_{i} \leq 2 \times 10^{5}
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N L
A_{1} A_{2} \cdots A_{N}
```

### Output

Print N lines. The k-th line should contain `-1` if no sequence B satisfies the condition for i=k; otherwise, it should contain the minimum value of \max(B) for such a sequence B.

---

### Sample Input 1

```
2 4
10 5
```

### Sample Output 1

```
3
-1
```

For A\_{1} = 10,
if we take B = (1, 0, 2, 3), then \displaystyle \sum\_{j = 1} ^ {L - 1} \sum\_{k = j + 1} ^ {L} |B\_{j} - B\_{k}| = 10, where \max(B) = 3.
No non-negative integer sequence B satisfies the condition with \max(B) < 3, so print 3 in the first line.

For A\_{2} = 5,
there is no non-negative integer sequence B that satisfies the condition, so print `-1` in the second line.

---

### Sample Input 2

```
6 8
167 924 167167 167924 116677 154308
```

### Sample Output 2

```
11
58
10448
10496
7293
9645
```
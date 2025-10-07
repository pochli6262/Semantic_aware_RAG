Score: 600 points

### Problem Statement

You are given non-negative integers P and B. Here, P is prime, and 1 \leq B \leq P-1.  
For a sequence of non-negative integers X=(x\_1,x\_2,\dots,x\_n), the hash value \mathrm{hash}(X) is defined as follows.

\displaystyle \mathrm{hash}(X) = \left(\sum\_{i=1}^n x\_i B^{n-i}\right) \bmod P

You are given M pairs of integers (L\_1, R\_1), (L\_2, R\_2), \dots, (L\_M, R\_M).  
Is there a sequence of non-negative integers A=(A\_1, A\_2, \dots, A\_N) of length N that satisfies the condition below?

* For all i (1 \leq i \leq M), the following condition holds:
  + Let s be the sequence (A\_{L\_i}, A\_{L\_i + 1}, \dots, A\_{R\_i}) obtained by taking the L\_i-th to the R\_i-th elements of A. Then, \mathrm{hash}(s) \neq 0.

### Constraints

* 2 \leq P \leq 10^9
* P is prime.
* 1 \leq B \leq P - 1
* 1 \leq N \leq 16
* 1 \leq M \leq \frac{N(N+1)}{2}
* 1 \leq L\_i \leq R\_i \leq N
* (L\_i, R\_i) \neq (L\_j, R\_j) if i \neq j.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
P B N M
L_1 R_1
L_2 R_2
\vdots
L_M R_M
```

### Output

If there is a sequence that satisfies the condition in the problem statement, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3 2 3 3
1 1
1 2
2 3
```

### Sample Output 1

```
Yes
```

The sequence A = (2, 0, 4) satisfies the condition because \mathrm{hash}((A\_1)) = 2, \mathrm{hash}((A\_1, A\_2)) = 1, \mathrm{hash}((A\_2, A\_3)) = 1.

---

### Sample Input 2

```
2 1 3 3
1 1
2 3
1 3
```

### Sample Output 2

```
No
```

No sequence satisfies the condition.

---

### Sample Input 3

```
998244353 986061415 6 11
1 5
2 2
2 5
2 6
3 4
3 5
3 6
4 4
4 5
4 6
5 6
```

### Sample Output 3

```
Yes
```
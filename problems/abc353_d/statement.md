Score: 400 points

### Problem Statement

For positive integers x and y, define f(x, y) as follows:

* Interpret the decimal representations of x and y as strings and concatenate them in this order to obtain a string z. The value of f(x, y) is the value of z when interpreted as a decimal integer.

For example, f(3, 14) = 314 and f(100, 1) = 1001.

You are given a sequence of positive integers A = (A\_1, \ldots, A\_N) of length N. Find the value of the following expression modulo 998244353:

\displaystyle \sum\_{i=1}^{N-1}\sum\_{j=i+1}^N f(A\_i,A\_j).

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq 10^9
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
3 14 15
```

### Sample Output 1

```
2044
```

* f(A\_1, A\_2) = 314
* f(A\_1, A\_3) = 315
* f(A\_2, A\_3) = 1415

Thus, the answer is f(A\_1, A\_2) + f(A\_1, A\_3) + f(A\_2, A\_3) = 2044.

---

### Sample Input 2

```
5
1001 5 1000000 1000000000 100000
```

### Sample Output 2

```
625549048
```

Be sure to calculate the value modulo 998244353.
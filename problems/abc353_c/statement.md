Score: 300 points

### Problem Statement

For positive integers x and y, define f(x, y) as the remainder of (x + y) divided by 10^8.

You are given a sequence of positive integers A = (A\_1, \ldots, A\_N) of length N. Find the value of the following expression:

\displaystyle \sum\_{i=1}^{N-1}\sum\_{j=i+1}^N f(A\_i,A\_j).

### Constraints

* 2 \leq N \leq 3\times 10^5
* 1 \leq A\_i < 10^8
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
3 50000001 50000002
```

### Sample Output 1

```
100000012
```

* f(A\_1,A\_2)=50000004
* f(A\_1,A\_3)=50000005
* f(A\_2,A\_3)=3

Thus, the answer is f(A\_1,A\_2) + f(A\_1,A\_3) + f(A\_2,A\_3) = 100000012.

Note that you are not asked to compute the remainder of the sum divided by 10^8.

---

### Sample Input 2

```
5
1 3 99999999 99999994 1000000
```

### Sample Output 2

```
303999988
```
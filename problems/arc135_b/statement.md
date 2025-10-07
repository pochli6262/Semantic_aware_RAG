Score : 500 points

### Problem Statement

You are given a sequence of N integers S = (S\_1, \ldots, S\_N).
Determine whether there is a sequence of N+2 integers A = (A\_1, \ldots, A\_{N+2}) that satisfies the conditions below.

* 0\leq A\_i for every i (1\leq i\leq N+2).
* S\_i = A\_{i} + A\_{i+1} + A\_{i+2} for every i (1\leq i\leq N).

If it exists, print one such sequence.

### Constraints

* 1\leq N\leq 3\times 10^5
* 0\leq S\_i\leq 10^9

---

### Input

Input is given from Standard Input from the following format:

```
N
S_1 \ldots S_N
```

### Output

If there is a sequence A that satisfies the conditions, print `Yes`; otherwise, print `No`.
In the case of `Yes`, print an additional line containing the elements of such a sequence A, separated by spaces.

```
A_1 \ldots A_{N+2}
```

If there are multiple sequences satisfying the conditions, you may print any of them.

---

### Sample Input 1

```
5
6 9 6 6 5
```

### Sample Output 1

```
Yes
0 4 2 3 1 2 2
```

We can verify that S\_i = A\_i + A\_{i+1} + A\_{i+2} for every i (1\leq i\leq N), as follows.

* 6 = 0 + 4 + 2.
* 9 = 4 + 2 + 3.
* 6 = 2 + 3 + 1.
* 6 = 3 + 1 + 2.
* 5 = 1 + 2 + 2.

---

### Sample Input 2

```
5
0 1 2 1 0
```

### Sample Output 2

```
No
```

---

### Sample Input 3

```
1
10
```

### Sample Output 3

```
Yes
0 0 10
```
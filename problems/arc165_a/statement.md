Score : 400 points

### Problem Statement

You are given a positive integer N.

Determine if there are two or more (not necessarily distinct) positive integers A\_1,A\_2,\dots,A\_n\ (2 \leq n) that satisfy all of the following conditions:

* A\_1+A\_2+\dots+A\_n=N.
* The least common multiple of A\_1,A\_2,\dots,A\_n is N.

You have T test cases to solve.

### Constraints

* 1 \leq T \leq 100
* 2 \leq N \leq 10^{9}
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
T
\mathrm{case}_1
\vdots
\mathrm{case}_T
```

Each case is given in the following format:

```
N
```

### Output

Print T lines. The i-th line should contain `Yes` if some integers satisfy the conditions for the i-th test case, and `No` otherwise.

---

### Sample Input 1

```
4
6
4
998244353
367291763
```

### Sample Output 1

```
Yes
No
No
Yes
```

For the first test case, three positive integers (A\_1,A\_2,A\_3)=(1,2,3), for example, have A\_1+A\_2+A\_3=1+2+3=6, and the least common multiple of A\_1,A\_2,A\_3 is 6, satisfying the conditions.

For the second test case, no two or more positive integers satisfy the conditions.
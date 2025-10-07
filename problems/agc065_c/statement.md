Score : 900 points

### Problem Statement

You are given a sequence of non-negative integers A=(A\_1,A\_2,\dots,A\_N) of length N. Here, S=\sum\_{i=1}^{N} A\_i is even.

Determine whether there is a pair of sequences of non-negative integers of length N, B=(B\_1,B\_2,\dots,B\_N) and C=(C\_1,C\_2,\dots,C\_N), that satisfy the following conditions:

* B\_i+C\_i=A\_i for i=1,2,\dots,N.
* \sum\_{i=1}^{N} X\_i \neq \frac{S}{2} for every sequence of integers X=(X\_1,X\_2,\dots,X\_N) of length N where X\_i=B\_i or X\_i=C\_i for i=1,2,\dots,N.

Solve T test cases.

### Constraints

* 1 \leq T
* 1 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq 10^9
* \sum\_{i=1}^{N} A\_i is even.
* The sum of N over all test cases in a single input is at most 2 \times 10^5.
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
A_1 A_2 \dots A_N
```

### Output

Print T lines. The i-th line should contain `Yes` if there is a pair of sequences B and C that satisfy the conditions for the i-th test case, and `No` otherwise.

---

### Sample Input 1

```
3
3
1 2 3
6
1 1 2 2 3 3
4
1 1 1000000000 1000000000
```

### Sample Output 1

```
Yes
No
Yes
```

For the first test case, B=(1,1,3) and C=(0,1,0) satisfy the conditions.

For the second test case, no pair of B and C satisfies the conditions.
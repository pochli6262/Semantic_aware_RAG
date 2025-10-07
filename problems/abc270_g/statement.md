Score : 600 points

### Problem Statement

There is a sequence X=(X\_0, X\_1, \ldots) defined by the following recurrence relation.

X\_i = \left\{
\begin{array}{ll}
S & (i = 0)\\
(A X\_{i-1}+B) \bmod P & (i \geq 1)
\end{array}
\right.

Determine whether there is an i such that X\_i=G. If it exists, find the smallest such i.  
Here, x \bmod y denotes the remainder when x is divided by y (the least non-negative residue).

You are given T test cases for each input file.

### Constraints

* 1 \leq T \leq 100
* 2 \leq P \leq 10^9
* P is a prime.
* 0\leq A,B,S,G < P
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
T
\mathrm{case}_1
\mathrm{case}_2
\vdots
\mathrm{case}_T
```

Each test case is in the following format:

```
P A B S G
```

### Output

Print T lines.  
The t-th line should contain the smallest i such that X\_i=G for \mathrm{case}\_t, or `-1` if there is no such i.

---

### Sample Input 1

```
3
5 2 1 1 0
5 2 2 3 0
11 1 1 0 10
```

### Sample Output 1

```
3
-1
10
```

For the first test case, we have X=(1,3,2,0,\ldots), so the smallest i such that X\_i=0 is 3.  
For the second test case, we have X=(3,3,3,3,\ldots), so there is no i such that X\_i=0.
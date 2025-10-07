Score : 500 points

### Problem Statement

You are given a rooted tree with N vertices. The root is Vertex 1.  
For each i = 1, 2, \ldots, N-1, the i-th edge connects Vertex u\_i and Vertex v\_i.

For each i = 1, 2, \ldots, N, let S\_i denote the set of all vertices in the subtree rooted at Vertex i. (Each vertex is in the subtree rooted at itself, that is, i \in S\_i.)

Additionally, for integers l and r, let [l, r] denote the set of all integers between l and r, that is, [l, r] = \lbrace l, l+1, l+2, \ldots, r \rbrace.

Consider a sequence of N pairs of integers \big((L\_1, R\_1), (L\_2, R\_2), \ldots, (L\_N, R\_N)\big) that satisfies the conditions below.

* 1 \leq L\_i \leq R\_i for every integer i such that 1 \leq i \leq N.
* The following holds for every pair of integers (i, j) such that 1 \leq i, j \leq N.
  + [L\_i, R\_i] \subseteq [L\_j, R\_j] if S\_i \subseteq S\_j
  + [L\_i, R\_i] \cap [L\_j, R\_j] = \emptyset if S\_i \cap S\_j = \emptyset

It can be shown that there is at least one sequence \big((L\_1, R\_1), (L\_2, R\_2), \ldots, (L\_N, R\_N)\big).
Among those sequences, print one that minimizes \max \lbrace L\_1, L\_2, \ldots, L\_N, R\_1, R\_2, \ldots, R\_N \rbrace, the maximum integer used. (If there are multiple such sequences, you may print any of them.)

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq u\_i, v\_i \leq N
* All values in input are integers.
* The given graph is a tree.

---

### Input

Input is given from Standard Input in the following format:

```
N
u_1 v_1
u_2 v_2
\vdots
u_{N-1} v_{N-1}
```

### Output

Print N lines in the format below. That is, for each i = 1, 2, \ldots, N, the i-th line should contain L\_i and R\_i separated by a space.

```
L_1 R_1
L_2 R_2
\vdots
L_N R_N
```

---

### Sample Input 1

```
3
2 1
3 1
```

### Sample Output 1

```
1 2
2 2
1 1
```

(L\_1, R\_1) = (1, 2), (L\_2, R\_2) = (2, 2), (L\_3, R\_3) = (1, 1) satisfies the conditions.  
Indeed, we have [L\_2, R\_2] \subseteq [L\_1, R\_1], [L\_3, R\_3] \subseteq [L\_1, R\_1], [L\_2, R\_2] \cap [L\_3, R\_3] = \emptyset.  
Additionally, \max \lbrace L\_1, L\_2, L\_3, R\_1, R\_2, R\_3 \rbrace = 2 is the minimum possible value.

---

### Sample Input 2

```
5
3 4
5 4
1 2
1 4
```

### Sample Output 2

```
1 3
3 3
2 2
1 2
1 1
```

---

### Sample Input 3

```
5
4 5
3 2
5 2
3 1
```

### Sample Output 3

```
1 1
1 1
1 1
1 1
1 1
```
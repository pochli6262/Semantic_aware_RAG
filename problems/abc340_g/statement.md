Score: 600 points

### Problem Statement

There is a tree T with N vertices numbered from 1 to N. The i-th edge connects vertices u\_i and v\_i. Additionally, vertex i is painted with color A\_i.  
Find the number, modulo 998244353, of (non-empty) subsets S of the vertex set of T that satisfy the following condition:

* The induced subgraph G of T by S satisfies all of the following conditions:
  + G is a tree.
  + All vertices with degree 1 have the same color.

What is an induced subgraph?
Let S be a subset of the vertices of a graph G. The induced subgraph of G by S is a graph whose vertex set is S and whose edge set consists of all edges in G that have both endpoints in S.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq N
* 1 \leq u\_i \lt v\_i \leq N
* The graph given in the input is a tree.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
u_1 v_1
u_2 v_2
\vdots
u_{N-1} v_{N-1}
```

### Output

Print the number, modulo 998244353, of (non-empty) subsets S of the vertex set of T that satisfy the condition in the problem statement.

---

### Sample Input 1

```
3
1 2 1
1 2
2 3
```

### Sample Output 1

```
4
```

The following four sets of vertices satisfy the condition.

* \lbrace 1 \rbrace
* \lbrace 1, 2, 3 \rbrace
* \lbrace 2 \rbrace
* \lbrace 3 \rbrace

---

### Sample Input 2

```
5
2 2 1 1 1
2 5
3 4
1 3
1 5
```

### Sample Output 2

```
9
```

---

### Sample Input 3

```
15
5 3 5 1 1 4 4 4 2 5 5 4 4 2 5
3 13
4 10
7 11
8 9
2 10
2 14
5 11
5 6
6 13
12 13
9 14
9 13
1 13
1 15
```

### Sample Output 3

```
48
```
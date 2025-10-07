Score: 700 points

### Problem Statement

You are given a directed graph G with N vertices and M edges. The vertices are numbered from 1 to N, and each edge is labeled with `(` or `)`. The i-th edge is directed from vertex u\_i to vertex v\_i with a label c\_i. The graph does not contain multi-edges or self-loops.

In this graph, for any two vertices s and t, there is a path from s to t.

Determine if there is a **walk** on the graph G that satisfies all of the following conditions:

* The start and end vertices of the walk are the same.
* For i=1,2,\dots,M, the i-th edge is used at least once in the walk.
* The string obtained by arranging the labels of the edges used in the walk in the order of their usage is a regular bracket sequence.

What is a walk?
A walk on a graph G is a sequence (v\_1,e\_1,v\_2,\dots,v\_{k-1},e\_{k-1},v\_k) of k vertices (k is a positive integer) and k-1 edges, where the edge e\_i is directed from vertex v\_i to vertex v\_{i+1}. The vertices v\_1 and v\_k are called the start and end vertices of the walk, respectively.

What is a regular bracket sequence?

A regular bracket sequence is a string that satisfies one of the following conditions:

* It is an empty string.
* It is a string obtained by concatenating `(`, a regular bracket sequence A, and `)` in this order.
* It is a string obtained by concatenating two non-empty regular bracket sequences A and B in this order.

### Constraints

* 2 \leq N \leq 4000
* N \leq M \leq 8000
* 1 \leq u\_i,v\_i \leq N
* c\_i is `(` or `)`.
* u\_i \neq v\_i
* If i \neq j, then (u\_i,v\_i) \neq (u\_j,v\_j).
* All input values are integers.
* In the input graph, for any two vertices s and t, there is a path from s to t.

---

### Input

The input is given from Standard Input in the following format:

```
N M
u_1 v_1 c_1
u_2 v_2 c_2
\vdots
u_M v_M c_M
```

### Output

If there is a walk satisfying the conditions, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
5 7
1 2 (
2 3 )
3 4 (
4 1 )
2 4 )
4 5 (
5 1 )
```

### Sample Output 1

```
Yes
```

The walk that uses edges 1,2,3,4,1,5,6,7 in this order uses all the edges at least once, and the string `()()()()` obtained by arranging the labels of the edges in the order of their usage is a regular bracket sequence, so all conditions are satisfied.

The walk may use the same edge multiple times or visit the same vertex multiple times.

---

### Sample Input 2

```
2 2
1 2 )
2 1 )
```

### Sample Output 2

```
No
```

---

### Sample Input 3

```
10 20
4 5 (
5 6 (
6 7 )
2 5 )
5 8 (
6 3 )
8 5 )
1 2 (
9 10 (
4 7 (
3 4 )
8 9 (
2 1 )
1 4 )
2 3 )
3 2 (
7 8 (
7 4 )
10 9 )
9 8 )
```

### Sample Output 3

```
Yes
```
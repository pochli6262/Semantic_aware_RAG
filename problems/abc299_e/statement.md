Score : 500 points

### Problem Statement

You are given a simple connected undirected graph with N vertices and M edges (a simple graph contains no self-loop and no multi-edges).  
For i = 1, 2, \ldots, M, the i-th edge connects vertex u\_i and vertex v\_i bidirectionally.

Determine whether there is a way to paint each vertex black or white to satisfy both of the following conditions, and show one such way if it exists.

* At least one vertex is painted black.
* For every i = 1, 2, \ldots, K, the following holds:
  + the minimum distance between vertex p\_i and a vertex painted black is exactly d\_i.

Here, the distance between vertex u and vertex v is the minimum number of edges in a path connecting u and v.

### Constraints

* 1 \leq N \leq 2000
* N-1 \leq M \leq \min\lbrace N(N-1)/2, 2000 \rbrace
* 1 \leq u\_i, v\_i \leq N
* 0 \leq K \leq N
* 1 \leq p\_1 \lt p\_2 \lt \cdots \lt p\_K \leq N
* 0 \leq d\_i \leq N
* The given graph is simple and connected.
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
u_1 v_1
u_2 v_2
\vdots
u_M v_M
K
p_1 d_1
p_2 d_2
\vdots
p_K d_K
```

### Output

If there is no way to paint each vertex black or white to satisfy the conditions, print `No`.  
Otherwise, print `Yes` in the first line, and a string S representing a coloring of the vertices in the second line, as shown below.  
Here, S is a string of length N such that, for each i = 1, 2, \ldots, N, the i-th character of S is 1 if vertex i is painted black and 0 if white.

```
Yes
S
```

If multiple solutions exist, you may print any of them.

---

### Sample Input 1

```
5 5
1 2
2 3
3 1
3 4
4 5
2
1 0
5 2
```

### Sample Output 1

```
Yes
10100
```

One way to satisfy the conditions is to paint vertices 1, 3 black and vertices 2, 4, 5 white.  
Indeed, for each i = 1, 2, 3, 4, 5, let A\_i denote the minimum distance between vertex i and a vertex painted black, and we have (A\_1, A\_2, A\_3, A\_4, A\_5) = (0, 1, 0, 1, 2), where A\_1 = 0, A\_5 = 2.

---

### Sample Input 2

```
5 5
1 2
2 3
3 1
3 4
4 5
5
1 1
2 1
3 1
4 1
5 1
```

### Sample Output 2

```
No
```

There is no way to satisfy the conditions by painting each vertex black or white, so you should print `No`.

---

### Sample Input 3

```
1 0
0
```

### Sample Output 3

```
Yes
1
```
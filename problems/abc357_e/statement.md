Score : 450 points

### Problem Statement

There is a directed graph with N vertices numbered 1 to N and N edges.  
The out-degree of every vertex is 1, and the edge from vertex i points to vertex a\_i.  
Count the number of pairs of vertices (u, v) such that vertex v is reachable from vertex u.

Here, vertex v is reachable from vertex u if there exists a sequence of vertices w\_0, w\_1, \dots, w\_K of length K+1 that satisfies the following conditions. In particular, if u = v, it is always reachable.

* w\_0 = u.
* w\_K = v.
* For every 0 \leq i \lt K, there is an edge from vertex w\_i to vertex w\_{i+1}.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq a\_i \leq N
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
a_1 a_2 \dots a_N
```

### Output

Print the number of pairs of vertices (u, v) such that vertex v is reachable from vertex u.

---

### Sample Input 1

```
4
2 1 1 4
```

### Sample Output 1

```
8
```

The vertices reachable from vertex 1 are vertices 1, 2.  
The vertices reachable from vertex 2 are vertices 1, 2.  
The vertices reachable from vertex 3 are vertices 1, 2, 3.  
The vertex reachable from vertex 4 is vertex 4.  
Therefore, the number of pairs of vertices (u, v) such that vertex v is reachable from vertex u is 8.  
Note that the edge from vertex 4 is a self-loop, that is, it points to vertex 4 itself.

---

### Sample Input 2

```
5
2 4 3 1 2
```

### Sample Output 2

```
14
```

---

### Sample Input 3

```
10
6 10 4 1 5 9 8 6 5 1
```

### Sample Output 3

```
41
```
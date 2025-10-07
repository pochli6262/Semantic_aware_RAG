Score : 475 points

### Problem Statement

There is a simple undirected graph with N vertices and M edges, where vertices are numbered from 1 to N, and edges are numbered from 1 to M. Edge i connects vertex a\_i and vertex b\_i.  
K security guards numbered from 1 to K are on some vertices. Guard i is on vertex p\_i and has a stamina of h\_i. All p\_i are distinct.

A vertex v is said to be **guarded** when the following condition is satisfied:

* there is at least one guard i such that the distance between vertex v and vertex p\_i is at most h\_i.

Here, the distance between vertex u and vertex v is the minimum number of edges in the path connecting vertices u and v.

List all guarded vertices **in ascending order**.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 0 \leq M \leq \min \left(\frac{N(N-1)}{2}, 2 \times 10^5 \right)
* 1 \leq K \leq N
* 1 \leq a\_i, b\_i \leq N
* The given graph is simple.
* 1 \leq p\_i \leq N
* All p\_i are distinct.
* 1 \leq h\_i \leq N
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M K
a_1 b_1
a_2 b_2
\vdots
a_M b_M
p_1 h_1
p_2 h_2
\vdots
p_K h_K
```

### Output

Print the answer in the following format. Here,

* G is the number of guarded vertices,
* and v\_1, v\_2, \dots, v\_G are the vertex numbers of the guarded vertices **in ascending order**.

```
G
v_1 v_2 \dots v_G
```

---

### Sample Input 1

```
5 5 2
1 2
2 3
2 4
3 5
1 5
1 1
5 2
```

### Sample Output 1

```
4
1 2 3 5
```

The guarded vertices are 1, 2, 3, 5.  
These vertices are guarded because of the following reasons.

* The distance between vertex 1 and vertex p\_1 = 1 is 0, which is not greater than h\_1 = 1. Thus, vertex 1 is guarded.
* The distance between vertex 2 and vertex p\_1 = 1 is 1, which is not greater than h\_1 = 1. Thus, vertex 2 is guarded.
* The distance between vertex 3 and vertex p\_2 = 5 is 1, which is not greater than h\_2 = 2. Thus, vertex 3 is guarded.
* The distance between vertex 5 and vertex p\_1 = 1 is 1, which is not greater than h\_1 = 1. Thus, vertex 5 is guarded.

---

### Sample Input 2

```
3 0 1
2 3
```

### Sample Output 2

```
1
2
```

The given graph may have no edges.

---

### Sample Input 3

```
10 10 2
2 1
5 1
6 1
2 4
2 5
2 10
8 5
8 6
9 6
7 9
3 4
8 2
```

### Sample Output 3

```
7
1 2 3 5 6 8 9
```
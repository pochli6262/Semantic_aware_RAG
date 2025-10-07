Score : 600 points

### Problem Statement

Given is an undirected graph with N vertices and M edges. The i-th edge connects Vertices A\_i and B\_i and has a weight of C\_i.

Initially, all vertices are painted black. You can do the following operation at most K times.

* Operation: choose any vertex v and any integer x. Paint red all vertices reachable from the vertex v by traversing edges whose weights are at most x, including v itself.

How many sets can be the set of vertices painted red after the operations?  
Find the count modulo 998244353.

### Constraints

* 2 \leq N \leq 10^5
* 0 \leq M \leq 10^5
* 1 \leq K \leq 500
* 1 \leq A\_i,B\_i \leq N
* 1 \leq C\_i \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M K
A_1 B_1 C_1
\vdots
A_M B_M C_M
```

### Output

Print the answer.

---

### Sample Input 1

```
3 2 1
1 2 1
2 3 2
```

### Sample Output 1

```
6
```

For example, an operation with (v,x)=(2,1) paints Vertices 1,2 red, and an operation with (v,x)=(1,0) paints Vertex 1.

After at most one operation, the set of vertices painted red can be one of the following six: \{\},\{1\},\{2\},\{3\},\{1,2\},\{1,2,3\}.

---

### Sample Input 2

```
5 0 2
```

### Sample Output 2

```
16
```

The given graph may not be connected.

---

### Sample Input 3

```
6 8 2
1 2 1
2 3 2
3 4 3
4 5 1
5 6 2
6 1 3
1 2 10
1 1 100
```

### Sample Output 3

```
40
```

The given graph may have multi-edges and self-loops.
Score : 300 points

### Problem Statement

You are given an N-by-N matrix A=(a\_{i,j}), where a\_{i,j} \in \{0,1\}.

We have the following directed graph.

* The graph has NK vertices numbered 1,2,\ldots,NK.
* The edges correspond to the NK-by-NK matrix X=(x\_{i,j}) obtained by arranging K^2 copies of A in K rows and K columns (see Sample Input/Output 1 for an example). If x\_{i,j}=1, there is a directed edge from vertex i to vertex j; if x\_{i,j}=0, that edge does not exist.

Answer the following question for i=1,2,\ldots,Q.

* Find the shortest length (number of edges) of a path from vertex s\_i to vertex t\_i. If there is no such path, print `-1` instead.

### Constraints

* 1 \leq N \leq 100
* 1 \leq K \leq 10^9
* a\_{i,j} \in \{0,1\}
* 1 \leq Q \leq 100
* 1 \leq s\_i,t\_i \leq NK
* s\_i \neq t\_i
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K
a_{1,1} \ldots a_{1,N}
\vdots
a_{N,1} \ldots a_{N,N}
Q
s_1 t_1
\vdots
s_Q t_Q
```

### Output

Print Q lines. The x-th line should contain the answer to the question for i=x.

---

### Sample Input 1

```
3 2
1 1 1
1 1 0
0 1 0
4
1 2
1 4
1 6
6 3
```

### Sample Output 1

```
1
1
1
3
```

Below is the matrix X representing the edges.

```
1 1 1 1 1 1
1 1 0 1 1 0
0 1 0 0 1 0
1 1 1 1 1 1
1 1 0 1 1 0
0 1 0 0 1 0
```

---

### Sample Input 2

```
4 1000000000
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1
1 4000000000
```

### Sample Output 2

```
-1
```

There is no edge.
Score : 600 points

### Problem Statement

We have a directed graph with N vertices, called Vertex 1, Vertex 2, \ldots, Vertex N.

For each pair of integers such that 1 \leq i, j \leq N and i \neq j, there is a directed edge from Vertex i to Vertex j of weight (A\_i + B\_j) \bmod M. (Here, x \bmod y denotes the remainder when x is divided by y.)

There is no edge other than the above.

Print the shortest distance from Vertex 1 to Vertex N, that is, the minimum possible total weight of the edges in a path from Vertex 1 to Vertex N.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 2 \leq M \leq 10^9
* 0 \leq A\_i, B\_j < M
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
A_1 A_2 \ldots A_N
B_1 B_2 \ldots B_N
```

### Output

Print the minimum possible total weight of the edges in a path from Vertex 1 to Vertex N.

---

### Sample Input 1

```
4 12
10 11 6 0
8 7 4 1
```

### Sample Output 1

```
3
```

Below, i \rightarrow j denotes the directed edge from Vertex i to Vertex j.  
Let us consider the path 1 \rightarrow 3 \rightarrow 2 \rightarrow 4.

* Edge 1\rightarrow 3 weighs (A\_1 + B\_3) \bmod M = (10 + 4) \bmod 12 = 2,
* Edge 3 \rightarrow 2 weighs (A\_3 + B\_2) \bmod M = (6 + 7) \bmod 12 = 1,
* Edge 2\rightarrow 4 weighs (A\_2 + B\_4) \bmod M = (11 + 1) \bmod 12 = 0.

Thus, the total weight of the edges in this path is 2 + 1 + 0 = 3.  
This is the minimum possible sum for a path from Vertex 1 to Vertex N.

---

### Sample Input 2

```
10 1000
785 934 671 520 794 168 586 667 411 332
363 763 40 425 524 311 139 875 548 198
```

### Sample Output 2

```
462
```
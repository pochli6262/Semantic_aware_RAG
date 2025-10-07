Score : 500 points

### Problem Statement

Given is a tree with N vertices.
The vertices are numbered 1, 2, \ldots, N, and for each 1\leq i\leq N-1, the i-th edge connects Vertex U\_i and Vertex V\_i.
Let D be the diameter of the tree. Find the number, modulo 998244353, of ways to choose two or more of the vertices and paint them red so that all distances between two red vertices are D.

Here, the distance between two vertices is the minimum number of edges that must be traversed to travel from one vertex to the other, and the diameter of the tree is the maximum distance between two vertices.

### Constraints

* 2 \leq N \leq 2\times 10^5
* 1 \leq U\_i,V\_i \leq N
* U\_i \neq V\_i
* All values in input are integers.
* The given graph is a tree.

---

### Input

Input is given from Standard Input in the following format:

```
N
U_1 V_1
U_2 V_2
\vdots
U_{N-1} V_{N-1}
```

### Output

Print the answer.

---

### Sample Input 1

```
5
1 2
1 3
1 4
4 5
```

### Sample Output 1

```
2
```

The given tree has five vertices and a diameter of 3.  
There are just two pairs of vertices whose distance is 3: (2,5) and (3,5), so there are two ways to paint the tree to satisfy the condition: \lbrace 2,5\rbrace  and \lbrace 3,5\rbrace .  
Note that painting 2,3,5 does not satisfy the condition since the distance between Vertex 2 and Vertex 3 is 2.

---

### Sample Input 2

```
4
1 2
1 3
1 4
```

### Sample Output 2

```
4
```

The diameter is 2, and the four ways to paint the tree to satisfy the condition are: \lbrace 2,3\rbrace , \lbrace 2,4\rbrace , \lbrace 3,4\rbrace , \lbrace 2,3,4\rbrace .
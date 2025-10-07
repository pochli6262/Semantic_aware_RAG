Score : 500 points

### Problem Statement

You are given a tree with N vertices. The vertices are numbered 1, \dots, N, and the i-th (1 \leq i \leq N - 1) edge connects Vertices A\_i and B\_i.

We define the **distance** between Vertices u and v on this tree by the number of edges in the shortest path from Vertex u to Vertex v.

You are given Q queries. In the i-th (1 \leq i \leq Q) query, given integers U\_i and K\_i, print the index of any vertex whose distance from Vertex U\_i is exactly K\_i. If there is no such vertex, print `-1`.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \lt B\_i \leq N \, (1 \leq i \leq N - 1)
* The given graph is a tree.
* 1 \leq Q \leq 2 \times 10^5
* 1 \leq U\_i, K\_i \leq N \, (1 \leq i \leq Q)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 B_1
\vdots
A_{N-1} B_{N-1}
Q
U_1 K_1
\vdots
U_Q K_Q
```

### Output

Print Q lines. The i-th (1 \leq i \leq Q) line should contain the index of any vertex whose distance from Vertex U\_i is exactly K\_i if such a vertex exists; if not, it should contain `-1`. If there are multiple such vertices, you may print any of them.

---

### Sample Input 1

```
5
1 2
2 3
3 4
3 5
3
2 2
5 3
3 3
```

### Sample Output 1

```
4
1
-1
```

* Two vertices, Vertices 4 and 5, have a distance exactly 2 from Vertex 2.
* Only Vertex 1 has a distance exactly 3 from Vertex 5.
* No vertex has a distance exactly 3 from Vertex 3.

---

### Sample Input 2

```
10
1 2
2 3
3 5
2 8
3 4
4 6
4 9
5 7
9 10
5
1 1
2 2
3 3
4 4
5 5
```

### Sample Output 2

```
2
4
10
-1
-1
```
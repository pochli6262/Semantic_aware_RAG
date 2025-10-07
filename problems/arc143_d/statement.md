Score : 700 points

### Problem Statement

We have two sequences A\_1,\ldots, A\_M and B\_1,\ldots,B\_M consisting of intgers between 1 and N (inclusive).

For a string of length M consisting of `0` and `1`, consider the following undirected graph with 2N vertices and (M+N) edges corresponding to that string.

* If the i-th character of the string is `0`, the i-th edge connects Vertex A\_i and Vertex (B\_i+N).
* If the i-th character of the string is `1`, the i-th edge connects Vertex B\_i and Vertex (A\_i+N).
* The (j+M)-th edge connects Vertex j and Vertex (j+N).

Here, i and j are integers such that 1 \leq i \leq M and 1 \leq j \leq N,
and the vertices are numbered 1 to 2N.

Find one string of length M consisting of `0` and `1` such that the corresponding undirected graph has the minimum number of bridges.

Notes on bridges
A bridge is an edge of a graph whose removal increases the number of connected components.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq M \leq 2 \times 10^5
* 1 \leq A\_i, B\_i \leq N

---

### Input

Input is given from Standard Input in the following format:

```
N M
A_1 A_2 \cdots A_M
B_1 B_2 \cdots B_M
```

### Output

Print one string that satisfies the requirement. If there are multiple such strings, you may print any of them.

---

### Sample Input 1

```
2 2
1 1
2 2
```

### Sample Output 1

```
01
```

The graph corresponding to `01` has no bridges.

In the graph corresponding to `00`, the edge connecting Vertex 1 and Vertex 3 and the edge connecting Vertex 2 and Vertex 4 are bridges, so `00` does not satisfy the requirement.

---

### Sample Input 2

```
6 7
1 1 2 3 4 4 5
2 3 3 4 5 6 6
```

### Sample Output 2

```
0100010
```
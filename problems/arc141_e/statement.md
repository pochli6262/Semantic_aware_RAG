Score : 700 points

### Problem Statement

There is an undirected graph with N^2 vertices. Initially, it has no edges. For each pair of integers (i,\ j) such that 0 \leq i,\ j < N, the graph has a corresponding vertex called (i,\ j).

You will get Q queries, which should be processed in order. The i-th query, which gives you four integers a\_i,\ b\_i,\ c\_i,\ d\_i, is as follows.

* For each k (0 \leq k < N), add an edge between two vertices ((a\_i+k) \bmod N,\ (b\_i+k) \bmod N) and ((c\_i+k) \bmod N,\ (d\_i+k) \bmod N). Then, print the current number of connected components in the graph.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq Q \leq 2 \times 10^5
* 0 \leq a\_i,\ b\_i,\ c\_i,\ d\_i < N
* (a\_i,\ b\_i) \neq (c\_i,\ d\_i)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N Q
a_1 b_1 c_1 d_1
a_2 b_2 c_2 d_2
\vdots
a_Q b_Q c_Q d_Q
```

### Output

Print Q lines. The i-th line should contain the number of connected components in the graph at the i-th query.

---

### Sample Input 1

```
3 3
0 0 1 2
2 0 0 0
1 1 2 2
```

### Sample Output 1

```
6
4
4
```

The first query adds an edge between (0,\ 0),\ (1,\ 2), between (1,\ 1),\ (2,\ 0), and between (2,\ 2),\ (0,\ 1), changing the number of connected components from 9 to 6.

---

### Sample Input 2

```
4 3
0 0 2 2
2 3 1 2
1 1 3 3
```

### Sample Output 2

```
14
11
11
```

The graph after queries may not be simple.

---

### Sample Input 3

```
6 5
0 0 1 1
1 2 3 4
1 1 5 3
2 0 1 5
5 0 3 3
```

### Sample Output 3

```
31
27
21
21
19
```
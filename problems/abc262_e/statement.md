Score : 500 points

### Problem Statement

You are given a simple undirected graph with N vertices and M edges. The vertices are numbered 1, \dots, N, and the i-th (1 \leq i \leq M) edge connects Vertices U\_i and V\_i.

There are 2^N ways to paint each vertex red or blue. Find the number, modulo 998244353, of such ways that satisfy all of the following conditions:

* There are exactly K vertices painted red.
* There is an even number of edges connecting vertices painted in different colors.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq M \leq 2 \times 10^5
* 0 \leq K \leq N
* 1 \leq U\_i \lt V\_i \leq N \, (1 \leq i \leq M)
* (U\_i, V\_i) \neq (U\_j, V\_j) \, (i \neq j)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M K
U_1 V_1
\vdots
U_M V_M
```

### Output

Print the answer.

---

### Sample Input 1

```
4 4 2
1 2
1 3
2 3
3 4
```

### Sample Output 1

```
2
```

The following two ways satisfy the conditions.

* Paint Vertices 1 and 2 red and Vertices 3 and 4 blue.
* Paint Vertices 3 and 4 red and Vertices 1 and 2 blue.

In either of the ways above, the 2-nd and 3-rd edges connect vertices painted in different colors.

---

### Sample Input 2

```
10 10 3
1 2
2 4
1 5
3 6
3 9
4 10
7 8
9 10
5 9
3 4
```

### Sample Output 2

```
64
```
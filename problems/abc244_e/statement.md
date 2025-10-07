Score : 500 points

### Problem Statement

You are given a simple undirected graph with N vertices and M edges. The vertices are numbered from 1 through N, and the edges are numbered from 1 through M. Edge i connects Vertex U\_i and Vertex V\_i.

You are given integers K, S, T, and X. How many sequences A = (A\_0, A\_1, \dots, A\_K) are there satisfying the following conditions?

* A\_i is an integer between 1 and N (inclusive).
* A\_0 = S
* A\_K = T
* There is an edge that directly connects Vertex A\_i and Vertex A\_{i+1}.
* Integer X\ (X≠S,X≠T) appears even number of times (possibly zero) in sequence A.

Since the answer can be very large, find the answer modulo 998244353.

### Constraints

* All values in input are integers.
* 2≤N≤2000
* 1≤M≤2000
* 1≤K≤2000
* 1≤S,T,X≤N
* X≠S
* X≠T
* 1≤U\_i<V\_i≤N
* If i ≠ j, then (U\_i, V\_i) ≠ (U\_j, V\_j).

---

### Input

Input is given from Standard Input in the following format:

```
N M K S T X
U_1 V_1
U_2 V_2
\vdots
U_M V_M
```

### Output

Print the answer modulo 998244353.

---

### Sample Input 1

```
4 4 4 1 3 2
1 2
2 3
3 4
1 4
```

### Sample Output 1

```
4
```

The following 4 sequences satisfy the conditions:

* (1, 2, 1, 2, 3)
* (1, 2, 3, 2, 3)
* (1, 4, 1, 4, 3)
* (1, 4, 3, 4, 3)

On the other hand, (1, 2, 3, 4, 3) and (1, 4, 1, 2, 3) do not, since there are odd number of occurrences of 2.

---

### Sample Input 2

```
6 5 10 1 2 3
2 3
2 4
4 6
3 6
1 5
```

### Sample Output 2

```
0
```

The graph is not necessarily connected.

---

### Sample Input 3

```
10 15 20 4 4 6
2 6
2 7
5 7
4 5
2 4
3 7
1 7
1 4
2 9
5 10
1 3
7 8
7 9
1 6
1 2
```

### Sample Output 3

```
952504739
```

Find the answer modulo 998244353.
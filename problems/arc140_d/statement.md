Score : 700 points

### Problem Statement

For an integer sequence X=(X\_1,X\_2,\dots,X\_N) of length N whose elements are all between 1 and N (inclusive), consider the question below, and let f(X) be the answer.

> There is an undirected graph G with N vertices (and possibly multi-edges and self-loops). G has N edges, the i-th of which connects Vertex i and Vertex X\_i. Find the number of connected components in G.

You are given an integer sequence A=(A\_1,A\_2,\dots,A\_N) of length N, where each A\_i is an integer between 1 and N (inclusive) or -1.

Consider an integer sequence X=(X\_1,X\_2,\dots,X\_N) of length N whose elements are all between 1 and N such that A\_i \neq -1 \Rightarrow A\_i = X\_i. Find the sum of f(X) over all such X, modulo 998244353.

### Constraints

* 1 \le N \le 2000
* A\_i is between 1 and N (inclusive) or -1.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

Prin the answer.

---

### Sample Input 1

```
3
-1 1 3
```

### Sample Output 1

```
5
```

There are three sequences X satisfying the requirement, as follows.

* X=(1,1,3), for which the answer to the question is 2.
* X=(2,1,3), for which the answer to the question is 2.
* X=(3,1,3), for which the answer to the question is 1.

Thus, the answer is 2+2+1=5.

---

### Sample Input 2

```
1
1
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
8
-1 3 -1 -1 8 -1 -1 -1
```

### Sample Output 3

```
433760
```
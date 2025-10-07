Score : 500 points

### Problem Statement

You are given an integer sequence A=(A\_1,A\_2,\dots,A\_N) of length N.

You can rearrange A freely. Find the maximum value that \sum\_{i=1}^{N-1} ((A\_{i+1} - A\_i) \bmod K) can take after rearranging.

Here, x \bmod K denotes the integer y such that 0 \le y < K and x - y is a multiple of K. For example, -3 \bmod 8 = 5, and 9 \bmod 6 = 3.

### Constraints

* 2 \le N \le 2 \times 10^5
* 1 \le K \le 10^9
* 0 \le A\_i < K

---

### Input

The input is given from Standard Input in the following format:

```
N K
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3 4
0 1 2
```

### Sample Output 1

```
6
```

One optimal solution is to rearrange A into (2,1,0) to achieve (1 - 2) \bmod 4 + (0 - 1) \bmod 4 = 3 + 3 = 6.

---

### Sample Input 2

```
7 123
11 34 56 0 32 100 78
```

### Sample Output 2

```
638
```
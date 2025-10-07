Score : 800 points

### Problem Statement

You are given an integer sequence of length N: A=(A\_1,A\_2,\dots,A\_N).

Find the K smallest positive integers X that satisfy the following condition.

* There is **no** non-empty (not necessarily contiguous) subsequence of A whose elements sum to X.

### Constraints

* 1 \leq N \leq 60
* 1 \leq K \leq 1000
* 1 \leq A\_i \leq 10^{15}
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K
A_1 A_2 \dots A_N
```

### Output

Print the K smallest positive integers satisfying the conditions in ascending order, separated by spaces.

---

### Sample Input 1

```
3 3
1 2 5
```

### Sample Output 1

```
4 9 10
```

The subsequences of A are (1),(2),(1,2),(5),(1,5),(2,5),(1,2,5), and their respective sums are 1,2,3,5,6,7,8. Therefore, for X=1,2,3,5,6,7,8, there are subsequences of A whose elements sum to X.

On the other hand, for X=4,9,10, there is no subsequence of A whose elements sum to X.

---

### Sample Input 2

```
20 10
324 60 1 15 60 15 1 60 319 1 327 1 2 60 2 345 1 2 2 15
```

### Sample Output 2

```
14 29 44 59 74 89 104 119 134 149
```
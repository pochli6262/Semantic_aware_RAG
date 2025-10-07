Score: 650 points

### Problem Statement

You are given 16 non-negative integers X\_{i, j, k, l} (i, j, k, l \in \lbrace 0, 1 \rbrace) in ascending order of (i, j, k, l).  
Let N = \displaystyle \sum\_{i=0}^1 \sum\_{j=0}^1 \sum\_{k=0}^1 \sum\_{l=0}^1 X\_{i,j,k,l}.  
Find the number, modulo 998244353, of sequences (A\_1, A\_2, ..., A\_{N+3}) of length N + 3 consisting of 0s and 1s that satisfy the following condition.

* For every quadruple of integers (i, j, k, l) (i, j, k, l \in \lbrace 0, 1 \rbrace), there are exactly X\_{i,j,k,l} integers s between 1 and N, inclusive, that satisfy:
  + A\_s = i, A\_{s + 1} = j, A\_{s + 2} = k, and A\_{s + 3} = l.

### Constraints

* X\_{i, j, k, l} are all non-negative integers.
* 1 \leq \displaystyle \sum\_{i=0}^1 \sum\_{j=0}^1 \sum\_{k=0}^1 \sum\_{l=0}^1 X\_{i,j,k,l} \leq 10^6

---

### Input

The input is given from Standard Input in the following format:

```
X_{0,0,0,0} X_{0,0,0,1} X_{0,0,1,0} X_{0,0,1,1} X_{0,1,0,0} X_{0,1,0,1} X_{0,1,1,0} X_{0,1,1,1} X_{1,0,0,0} X_{1,0,0,1} X_{1,0,1,0} X_{1,0,1,1} X_{1,1,0,0} X_{1,1,0,1} X_{1,1,1,0} X_{1,1,1,1} 
```

### Output

Print the number, modulo 998244353, of sequences that satisfy the condition in the problem statement.

---

### Sample Input 1

```
0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0
```

### Sample Output 1

```
1
```

This input corresponds to the case where X\_{1, 0, 1, 0} and X\_{1, 1, 0, 1} are 1 and all others are 0.  
In this case, only one sequence satisfies the condition, which is (1, 1, 0, 1, 0).

---

### Sample Input 2

```
1 1 2 0 1 2 1 1 1 1 1 2 1 0 1 0
```

### Sample Output 2

```
16
```

---

### Sample Input 3

```
21 3 3 0 3 0 0 0 4 0 0 0 0 0 0 0
```

### Sample Output 3

```
2024
```

---

### Sample Input 4

```
62 67 59 58 58 69 57 66 67 50 68 65 59 64 67 61
```

### Sample Output 4

```
741536606
```
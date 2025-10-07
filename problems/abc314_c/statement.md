Score : 300 points

### Problem Statement

You are given a string S of length N consisting of lowercase English letters.
Each character of S is painted in one of the M colors: color 1, color 2, ..., color M; for each i = 1, 2, \ldots, N, the i-th character of S is painted in color C\_i.

For each i = 1, 2, \ldots, M in this order, let us perform the following operation.

* Perform a right circular shift by 1 on the part of S painted in color i.
  That is, if the p\_1-th, p\_2-th, p\_3-th, \ldots, p\_k-th characters are painted in color i from left to right, then simultaneously replace the p\_1-th, p\_2-th, p\_3-th, \ldots, p\_k-th characters of S with the p\_k-th, p\_1-th, p\_2-th, \ldots, p\_{k-1}-th characters of S, respectively.

Print the final S after the above operations.

The constraints guarantee that at least one character of S is painted in each of the M colors.

### Constraints

* 1 \leq M \leq N \leq 2 \times 10^5
* 1 \leq C\_i \leq M
* N, M, and C\_i are all integers.
* S is a string of length N consisting of lowercase English letters.
* For each integer 1 \leq i \leq M, there is an integer 1 \leq j \leq N such that C\_j = i.

---

### Input

The input is given from Standard Input in the following format:

```
N M
S
C_1 C_2 \ldots C_N
```

### Output

Print the answer.

---

### Sample Input 1

```
8 3
apzbqrcs
1 2 3 1 2 2 1 2
```

### Sample Output 1

```
cszapqbr
```

Initially, S =  `apzbqrcs`.

* For i = 1, perform a right circular shift by 1 on the part of S formed by the 1-st, 4-th, 7-th characters, resulting in S =  `cpzaqrbs`.
* For i = 2, perform a right circular shift by 1 on the part of S formed by the 2-nd, 5-th, 6-th, 8-th characters, resulting in S =  `cszapqbr`.
* For i = 3, perform a right circular shift by 1 on the part of S formed by the 3-rd character, resulting in S =  `cszapqbr` (here, S is not changed).

Thus, you should print `cszapqbr`, the final S.

---

### Sample Input 2

```
2 1
aa
1 1
```

### Sample Output 2

```
aa
```
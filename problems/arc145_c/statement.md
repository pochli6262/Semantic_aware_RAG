Score : 600 points

### Problem Statement

The score of a permutation P=(P\_1,P\_2,\ldots,P\_{2N}) of (1,2,\ldots,2N) is defined as follows:

> Consider dividing P into two (not necessarily contiguous) subsequences A = (A\_1,A\_2,\ldots,A\_N) and B = (B\_1,B\_2,\ldots,B\_N). The score of P is the maximum possible value of \displaystyle\sum\_{i=1}^{N}A\_i B\_i in such a division.

Let M be the maximum among the scores of all permutations of (1,2,\ldots,2N).
Find the number, modulo 998244353, of permutations of (1,2,\ldots,2N) with the score of M.

### Constraints

* 1 \leq N \leq 2\times 10^5
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
```

### Output

Print the answer.

---

### Sample Input 1

```
2
```

### Sample Output 1

```
16
```

The maximum among the scores of the 24 possible permutations, M, is 14, and there are 16 permutations with the score of 14.

For instance, the permutation (1,2,3,4) achieves \sum \_{i=1}^{N}A\_i B\_i = 14 in the division A=(1,3), B=(2,4).

---

### Sample Input 2

```
10000
```

### Sample Output 2

```
391163238
```

Print the count modulo 998244353.
Score : 500 points

### Problem Statement

Given integers A, X, and M, find \displaystyle \sum\_{i = 0}^{X-1} A^i, modulo M.

### Constraints

* 1 \leq A, M \leq 10^9
* 1 \leq X \leq 10^{12}
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
A X M
```

### Output

Print the answer.

---

### Sample Input 1

```
3 4 7
```

### Sample Output 1

```
5
```

3^0 + 3^1 + 3^2 + 3^3 = 40, which equals 5 modulo 7, so 5 should be printed.

---

### Sample Input 2

```
8 10 9
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
1000000000 1000000000000 998244353
```

### Sample Output 3

```
919667211
```
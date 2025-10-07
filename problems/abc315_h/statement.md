Score : 650 points

### Problem Statement

You are given a sequence (A\_1, A\_2, \ldots , A\_N).
Let us define a sequence (F\_0, F\_1, \ldots , F\_N) by the following formulae.

* F\_0 = 1
* F\_n = A\_n\displaystyle\sum\_{i+j<n}F\_iF\_j (1 \leq n \leq N)

Find F\_1, \ldots , F\_N modulo 998244353.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 0 \leq A\_i < 998244353
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
```

### Output

Print F\_1, \ldots , F\_N modulo 998244353 in this order, with spaces in between.

---

### Sample Input 1

```
5
1 2 3 4 5
```

### Sample Output 1

```
1 6 48 496 6240
```

F\_1 = A\_1F\_0F\_0 = 1.
F\_2 = A\_2(F\_0F\_0+F\_0F\_1+F\_1F\_0) = 6.
Similarly, we find F\_3 = 48, F\_4 = 496, F\_5 = 6240.

---

### Sample Input 2

```
3
12345 678901 2345678
```

### Sample Output 2

```
12345 790834943 85679169
```
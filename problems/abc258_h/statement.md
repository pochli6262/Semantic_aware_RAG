Score : 600 points

### Problem Statement

Find the number, modulo 998244353, of sequences X that satisfy all of the following conditions.

* Every term in X is a positive **odd number**.
* The sum of the terms in X is S.
* The prefix sums of X contain none of A\_1, \dots, A\_N. Formally, if we define Y\_i = X\_1 + \dots + X\_i for each i, then Y\_i \neq A\_j holds for all integers i and j such that 1 \leq i \leq |X| and 1 \leq j \leq N.

### Constraints

* 1 \leq N \leq 10^5
* 1 \leq A\_1 \lt A\_2 \lt \dots \lt A\_N \lt S \leq 10^{18}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N S
A_1 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3 7
2 4 5
```

### Sample Output 1

```
3
```

The following three sequences satisfy the conditions.

* (1, 5, 1)
* (3, 3, 1)
* (7)

---

### Sample Input 2

```
5 60
10 20 30 40 50
```

### Sample Output 2

```
37634180
```

---

### Sample Input 3

```
10 1000000000000000000
1 2 4 8 16 32 64 128 256 512
```

### Sample Output 3

```
75326268
```
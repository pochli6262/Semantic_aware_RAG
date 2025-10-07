Score : 600 points

### Problem Statement

Given are positive integers N, M, and a sequence of positive integers D = (D\_1, \dots, D\_N).

Find the number of sequences of positive integers A = (A\_1, \dots, A\_N) that satisfy the following conditions, modulo 998244353.

* 1 \leq A\_i \leq M \, (1 \leq i \leq N)
* A\_i \neq A\_j \, (1 \leq i \lt j \leq N)
* For each i \, (1 \leq i \leq N), A\_i is a multiple of D\_i.

### Constraints

* 2 \leq N \leq 16
* 1 \leq M \leq 10^{18}
* 1 \leq D\_i \leq M \, (1 \leq i \leq N)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
D_1 \ldots D_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3 7
2 3 4
```

### Sample Output 1

```
3
```

The three sequences A that satisfy the conditions are (2, 3, 4), (2, 6, 4), (6, 3, 4).

---

### Sample Input 2

```
3 3
1 2 2
```

### Sample Output 2

```
0
```

No sequence A satisfies the conditions.

---

### Sample Input 3

```
6 1000000000000000000
380214083 420492929 929717250 666796775 209977152 770361643
```

### Sample Output 3

```
325683519
```

Be sure to find the count modulo 998244353.
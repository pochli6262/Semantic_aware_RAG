Score : 600 points

### Problem Statement

Find the number, modulo 998244353, of integer sequences A = (A\_1, \dots, A\_N) of length N that satisfy all of the following conditions:

* 0 \leq A\_i \leq M for all i such that 1 \leq i \leq N.
* The maximum value of A\_{L\_j}, \dots, A\_{R\_j} is X\_j for all j such that 1 \leq j \leq Q.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq M \lt 998244353
* 1 \leq Q \leq 2 \times 10^5
* 1 \leq L\_i \leq R\_i \leq N \, (1 \leq i \leq Q)
* 1 \leq X\_i \leq M \, (1 \leq i \leq Q)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M Q
L_1 R_1 X_1
\vdots
L_Q R_Q X_Q
```

### Output

Print the answer.

---

### Sample Input 1

```
3 3 2
1 2 2
2 3 3
```

### Sample Output 1

```
5
```

A = (0, 2, 3), (1, 2, 3), (2, 0, 3), (2, 1, 3), (2, 2, 3) satisfy the conditions.

---

### Sample Input 2

```
1 1 1
1 1 1
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
6 40000000 3
1 4 30000000
2 6 20000000
3 5 10000000
```

### Sample Output 3

```
135282163
```
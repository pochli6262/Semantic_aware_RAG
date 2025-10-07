Score : 600 points

### Problem Statement

Determine whether there is a sequence of N integers X = (X\_1, X\_2, \ldots ,X\_N) that satisfies all of the following conditions, and construct one such sequence if it exists.

* 0 \leq X\_i \leq M for every 1 \leq i \leq N.
* L\_i \leq X\_{A\_i} + X\_{B\_i} \leq R\_i for every 1 \leq i \leq Q.

### Constraints

* 1 \leq N \leq 10000
* 1 \leq M \leq 100
* 1 \leq Q \leq 10000
* 1 \leq A\_i, B\_i \leq N
* 0 \leq L\_i \leq R\_i \leq 2 \times M
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M Q
A_1 B_1 L_1 R_1
A_2 B_2 L_2 R_2
\vdots
A_Q B_Q L_Q R_Q
```

### Output

If there is an integer sequence that satisfies all of the conditions in the Problem Statement, print the elements X\_1, X\_2, \ldots, X\_N of one such sequence, separated by spaces. Otherwise, print `-1`.

---

### Sample Input 1

```
4 5 3
1 3 5 7
1 4 1 2
2 2 3 8
```

### Sample Output 1

```
2 4 3 0
```

For X = (2,4,3,0), we have X\_1 + X\_3 = 5, X\_1 + X\_4 = 2, and X\_2 + X\_2 = 8, so all conditions are satisfied. There are other sequences, such as X = (0,2,5,2) and X = (1,3,4,1), that satisfy all conditions, and those will also be accepted.

---

### Sample Input 2

```
3 7 3
1 2 3 4
3 1 9 12
2 3 2 4
```

### Sample Output 2

```
-1
```

No sequence X satisfies all conditions.
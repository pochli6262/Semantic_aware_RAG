Score : 300 points

### Problem Statement

You are given positive integers N and M. Find the maximum positive integer X that satisfies all of the following conditions.

* X is a positive integer less than 10^N, and all digits in the decimal representation of X are the same.
* X is a multiple of M.

If no positive integer X satisfies the conditions, print `-1`.

### Constraints

* 1\leq N\leq 10^5
* 1\leq M\leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N M
```

### Output

Print the maximum positive integer X that satisfies all of the conditions, or `-1` if no such positive integer X exists.

---

### Sample Input 1

```
7 12
```

### Sample Output 1

```
888888
```

Four positive integers X satisfy the conditions: 444, 888, 444444, 888888. The answer is the maximum of them, which is 888888.

---

### Sample Input 2

```
9 12
```

### Sample Output 2

```
888888888
```

Six positive integers X satisfy the conditions: 444, 888, 444444, 888888, 444444444, 888888888.

---

### Sample Input 3

```
1 3
```

### Sample Output 3

```
9
```

Three positive integers X satisfy the conditions: 3, 6, 9.

---

### Sample Input 4

```
1000 25
```

### Sample Output 4

```
-1
```

No positive integers X satisfy the conditions.

---

### Sample Input 5

```
30 1
```

### Sample Output 5

```
999999999999999999999999999999
```
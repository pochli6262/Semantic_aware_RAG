Score: 525 points

### Problem Statement

You are given integers X and Y, which satisfy at least one of X \neq 0 and Y \neq 0.  
Find a pair of integers (A, B) that satisfies all of the following conditions. If no such pair exists, report so.

* -10^{18} \leq A, B \leq 10^{18}
* The area of the triangle with vertices at points (0, 0), (X, Y), (A, B) on the xy-plane is 1.

### Constraints

* -10^{17} \leq X, Y \leq 10^{17}
* (X, Y) \neq (0, 0)
* X and Y are integers.

---

### Input

The input is given from Standard Input in the following format:

```
X Y
```

### Output

If there is a pair of integers (A, B) that satisfies the conditions, print it in the following format:

```
A B
```

Otherwise, print `-1`.

---

### Sample Input 1

```
3 5
```

### Sample Output 1

```
1 1
```

The area of the triangle with vertices at points (0, 0), (3, 5), (1, 1) is 1. Thus, (A, B) = (1, 1) satisfies the conditions.

---

### Sample Input 2

```
-2 0
```

### Sample Output 2

```
0 1
```

---

### Sample Input 3

```
8752654402832944 -6857065241301125
```

### Sample Output 3

```
-1
```
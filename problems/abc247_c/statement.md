Score : 300 points

### Problem Statement

We define sequences S\_n as follows.

* S\_1 is a sequence of length 1 containing a single 1.
* S\_n (n is an integer greater than or equal to 2) is a sequence obtained by concatenating S\_{n-1}, n, S\_{n-1} in this order.

For example, S\_2 and S\_3 is defined as follows.

* S\_2 is a concatenation of S\_1, 2, and S\_1, in this order, so it is 1,2,1.
* S\_3 is a concatenation of S\_2, 3, and S\_2, in this order, so it is 1,2,1,3,1,2,1.

Given N, print the entire sequence S\_N.

### Constraints

* N is an integer.
* 1 \leq N \leq 16

---

### Input

Input is given from Standard Input in the following format:

```
N
```

### Output

Print S\_N, with spaces in between.

---

### Sample Input 1

```
2
```

### Sample Output 1

```
1 2 1
```

As described in the Problem Statement, S\_2 is 1,2,1.

---

### Sample Input 2

```
1
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
4
```

### Sample Output 3

```
1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
```

* S\_4 is a concatenation of S\_3, 4, and S\_3, in this order.
Score: 300 points

### Problem Statement

A non-negative integer n is called a **good integer** when it satisfies the following condition:

* All digits in the decimal notation of n are even numbers (0, 2, 4, 6, and 8).

For example, 0, 68, and 2024 are good integers.

You are given an integer N. Find the N-th smallest good integer.

### Constraints

* 1 \leq N \leq 10^{12}
* N is an integer.

---

### Input

The input is given from Standard Input in the following format:

```
N
```

### Output

Print the N-th smallest good integer.

---

### Sample Input 1

```
8
```

### Sample Output 1

```
24
```

The good integers in ascending order are 0, 2, 4, 6, 8, 20, 22, 24, 26, 28, \dots.  
The eighth smallest is 24, which should be printed.

---

### Sample Input 2

```
133
```

### Sample Output 2

```
2024
```

---

### Sample Input 3

```
31415926535
```

### Sample Output 3

```
2006628868244228
```
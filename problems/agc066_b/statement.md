Score: 600 points

### Problem Statement

For a positive integer x, let f(x) denote the sum of its digits. For example, f(331)=3+3+1=7, f(2024)=2+0+2+4=8, and f(1)=1.

You are given a positive integer N. Print a positive integer x that satisfies all of the following conditions:

* 1\leq x< 10^{10000}
* f(2^{i-1}x)>f(2^ix) for all integers 1\leq i\leq N.

### Constraints

* 1\leq N\leq 50

---

### Input

The input is given from Standard Input in the following format:

```
N
```

### Output

Print a positive integer x that satisfies the conditions. If multiple positive integers x satisfy the conditions, any of them will be accepted.

---

### Sample Input 1

```
3
```

### Sample Output 1

```
89
```

For x=89, it follows from f(x)=17, f(2x)=16, f(4x)=14, and f(8x)=10 that f(x)>f(2x)>f(4x)>f(8x), satisfying the conditions.

Some other integers that satisfy the conditions are x=539 and x=890.
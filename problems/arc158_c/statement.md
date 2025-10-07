Score : 500 points

### Problem Statement

For a positive integer x, let f(x) denote the sum of its digits. For instance, f(158) = 1 + 5 + 8 = 14, f(2023) = 2 + 0 + 2 + 3 = 7, and f(1) = 1.

You are given a sequence of positive integers A = (A\_1, \ldots, A\_N). Find \sum\_{i=1}^N\sum\_{j=1}^N f(A\_i + A\_j).

### Constraints

* 1\leq N\leq 2\times 10^5
* 1\leq A\_i < 10^{15}

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 \ldots A_N
```

### Output

Print \sum\_{i=1}^N\sum\_{j=1}^N f(A\_i + A\_j).

---

### Sample Input 1

```
2
53 28
```

### Sample Output 1

```
36
```

We have \sum\_{i=1}^N\sum\_{j=1}^N f(A\_i + A\_j) = f(A\_1+A\_1)+f(A\_1+A\_2)+f(A\_2+A\_1)+f(A\_2+A\_2)=7+9+9+11=36.

---

### Sample Input 2

```
1
999999999999999
```

### Sample Output 2

```
135
```

We have \sum\_{i=1}^N\sum\_{j=1}^N f(A\_i + A\_j) = f(A\_1+A\_1) = 135.

---

### Sample Input 3

```
5
123 456 789 101 112
```

### Sample Output 3

```
321
```
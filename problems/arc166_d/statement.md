Score : 600 points

### Problem Statement

You are given positive integers x\_1, \ldots, x\_N such that x\_1 < \cdots < x\_N, and positive integers y\_1, \ldots, y\_N.

Consider a tuple (M, L\_1, R\_1, \ldots, L\_M, R\_M) that satisfies all of the following conditions.

* M is a positive integer.
* For each j \ (1\leq j\leq M), L\_j and R\_j are integers such that L\_j\leq R\_j.
* For each i \ (1\leq i\leq N), exactly y\_i integers j \ (1\leq j\leq M) satisfy L\_j\leq x\_i\leq R\_j.

It can be proved that such a tuple always exists. Find the maximum value of \min \lbrace R\_j-L\_j\mid 1\leq j\leq M\rbrace for such a tuple. If there is no maximum value, print `-1`.

### Constraints

* 1\leq N\leq 2\times 10^5
* 1\leq x\_1 < \cdots < x\_N \leq 10^9
* 1\leq y\_i \leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N
x_1 \cdots x_N
y_1 \cdots y_N
```

### Output

Print the maximum value of \min \lbrace R\_j-L\_j\mid 1\leq j\leq M\rbrace for a tuple that satisfies the conditions, or `-1` if there is no maximum value.

---

### Sample Input 1

```
3
1 3 5
1 3 1
```

### Sample Output 1

```
2
```

For example, we have \min \lbrace R\_j-L\_j\mid 1\leq j\leq M\rbrace = 2 for the tuple (3, 1, 4, 2, 4, 3, 5).

---

### Sample Input 2

```
3
1 10 100
2 3 2
```

### Sample Output 2

```
-1
```

For example, we have \min \lbrace R\_j-L\_j\mid 1\leq j\leq M\rbrace = 990 for the tuple (3, -1000, 10, -1000, 1000, 10, 1000). There is no maximum value of \min \lbrace R\_j-L\_j\mid 1\leq j\leq M\rbrace.

---

### Sample Input 3

```
7
10 31 47 55 68 73 90
3 7 4 6 3 4 4
```

### Sample Output 3

```
56
```
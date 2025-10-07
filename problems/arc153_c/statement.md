Score : 600 points

### Problem Statement

You are given a sequence of length N, A = (A\_1, \ldots, A\_N), consisting of 1 and -1.

Determine whether there is an integer sequence x = (x\_1, \ldots, x\_N) that satisfies all of the following conditions, and print one such sequence if it exists.

* |x\_i| \leq 10^{12} for every i (1\leq i\leq N).
* x is strictly increasing. That is, x\_1 < \cdots < x\_N.
* \sum\_{i=1}^N A\_ix\_i = 0.

### Constraints

* 1\leq N\leq 2\times 10^5
* A\_i \in \lbrace 1, -1\rbrace

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 \ldots A_N
```

### Output

If there is an integer sequence x that satisfies all of the conditions in question, print `Yes`; otherwise, print `No`. In case of `Yes`, print the elements of such an integer sequence x in the subsequent line, separated by spaces.

```
x_1 \ldots x_N
```

If multiple integer sequences satisfy the conditions, you may print any of them.

---

### Sample Input 1

```
5
-1 1 -1 -1 1
```

### Sample Output 1

```
Yes
-3 -1 4 5 7
```

For this output, we have \sum\_{i=1}^NA\_ix\_i= -(-3) + (-1) - 4 - 5 + 7 = 0.

---

### Sample Input 2

```
1
-1
```

### Sample Output 2

```
Yes
0
```

---

### Sample Input 3

```
2
1 -1
```

### Sample Output 3

```
No
```
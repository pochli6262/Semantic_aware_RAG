Score: 575 points

### Problem Statement

You are given an integer sequence A = (A\_1, A\_2, \ldots, A\_N).

Find the number of pairs of integers (L, R) that satisfy the following conditions:

* 1 \leq L \leq R \leq N
* There is a number that appears exactly once among A\_L, A\_{L + 1}, \ldots, A\_R. More precisely, there is an integer x such that exactly one integer i satisfies A\_i = x and L \leq i \leq R.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq N
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
5
2 2 1 2 1
```

### Sample Output 1

```
12
```

12 pairs of integers satisfy the conditions: (L, R) = (1, 1), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5), (5, 5).

---

### Sample Input 2

```
4
4 4 4 4
```

### Sample Output 2

```
4
```

---

### Sample Input 3

```
10
1 2 1 4 3 3 3 2 2 4
```

### Sample Output 3

```
47
```
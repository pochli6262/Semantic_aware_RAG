Score : 1000 points

### Problem Statement

Given is a sequence of N positive integers A = (A\_1, A\_2, \ldots, A\_N).

You can do the following operation on this sequence any number of times.

* Choose integers i, j, k such that 1\leq i < j < k \leq N and j = \frac{i+k}{2}. Replace A\_j with \lfloor\frac{A\_i+A\_k}{2}\rfloor.

Find the minimum possible value of \sum\_{i=1}^N A\_i after the operations.

### Constraints

* 3\leq N\leq 3\times 10^5
* 1\leq A\_i\leq 10^{12}

---

### Input

Input is given from Standard Input in the following format:

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
2 2 5 5 4
```

### Sample Output 1

```
13
```

The following operations achieves \sum\_{i=1}^N A\_i = 13.

* Do the operation with (i,j,k) = (1,3,5). The sequence A is now (2,2,3,5,4).
* Do the operation with (i,j,k) = (3,4,5). The sequence A is now (2,2,3,3,4).
* Do the operation with (i,j,k) = (2,3,4). The sequence A is now (2,2,2,3,4).

---

### Sample Input 2

```
5
3 1 4 1 5
```

### Sample Output 2

```
11
```

---

### Sample Input 3

```
3
3 1 3
```

### Sample Output 3

```
7
```

---

### Sample Input 4

```
3
3 5 3
```

### Sample Output 4

```
9
```
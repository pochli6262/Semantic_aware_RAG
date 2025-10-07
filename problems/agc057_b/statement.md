Score : 700 points

### Problem Statement

You are given a sequence A = (A\_1, A\_2, \ldots, A\_N) of positive integers and a positive integer X.
You can perform the operation below any number of times, possibly zero:

* Choose an index i (1\leq i\leq N) and a non-negative integer x such that 0\leq x\leq X. Change A\_i to 2A\_i+x.

Find the smallest possible value of \max\{A\_1,A\_2,\ldots,A\_N\}-\min\{A\_1,A\_2,\ldots,A\_N\} after your operations.

### Constraints

* 2\leq N\leq 10^5
* 1\leq X\leq 10^9
* 1\leq A\_i\leq 10^9

---

### Input

Input is given from Standard Input in the following format:

```
N X
A_1 A_2 \ldots A_N
```

### Output

Print the smallest possible value of \max\{A\_1,A\_2,\ldots,A\_N\}-\min\{A\_1,A\_2,\ldots,A\_N\} after your operations.

---

### Sample Input 1

```
4 2
5 8 12 20
```

### Sample Output 1

```
6
```

Let (i, x) denote an operation that changes A\_i to 2A\_i+x. An optimal sequence of operations is

* (1,0), (1,1), (2,2), (3,0)

which yields A = (21, 18, 24, 20), achieving \max\{A\_1,A\_2,A\_3,A\_4\}-\min\{A\_1,A\_2,A\_3,A\_4\} = 6.

---

### Sample Input 2

```
4 5
24 25 26 27
```

### Sample Output 2

```
0
```

An optimal sequence of operations is

* (1,5), (1,5), (2,5), (2,1), (3,2), (3,3), (4,0), (4,3)

which yields A = (111,111,111,111), achieving \max\{A\_1,A\_2,A\_3,A\_4\}-\min\{A\_1,A\_2,A\_3,A\_4\} = 0.

---

### Sample Input 3

```
4 1
24 25 26 27
```

### Sample Output 3

```
3
```

Performing no operations achieves \max\{A\_1,A\_2,A\_3,A\_4\}-\min\{A\_1,A\_2,A\_3,A\_4\} = 3.

---

### Sample Input 4

```
10 5
39 23 3 7 16 19 40 16 33 6
```

### Sample Output 4

```
13
```
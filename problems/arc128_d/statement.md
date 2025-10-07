Score : 700 points

### Problem Statement

We have N balls arranged in a row, numbered 1 to N from left to right.
Ball i has an integer A\_i written on it.

You can do the following operation any number of times.

* Choose three consecutive balls x, y, z (1 \leq x < y < z \leq N).
  Here, A\_x \neq A\_y and A\_y \neq A\_z must hold.
  Then, eat Ball y.
  After this operation, Balls x and z are considered adjacent.

Find the number of possible sets of balls remaining in the end, modulo 998244353.

### Constraints

* 2 \leq N \leq 200000
* 1 \leq A\_i \leq N
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 A_2 \cdots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4
1 2 1 2
```

### Sample Output 1

```
3
```

There are three possible sets of balls remaining in the end: \{1,2,3,4\},\{1,2,4\},\{1,3,4\}.

---

### Sample Input 2

```
5
5 4 3 2 1
```

### Sample Output 2

```
8
```

Different sequences of operations are not distinguished if they result in the same set of balls.

---

### Sample Input 3

```
5
1 2 3 2 1
```

### Sample Output 3

```
8
```

Different sets of remaining balls are distinguished even if they have the same sequence of integers written on them.

---

### Sample Input 4

```
9
1 4 2 2 9 6 9 6 6
```

### Sample Output 4

```
14
```
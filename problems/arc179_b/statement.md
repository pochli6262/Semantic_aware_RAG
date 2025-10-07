Score : 500 points

### Problem Statement

You are given a sequence (X\_1, X\_2, \dots, X\_M) of length M consisting of integers between 1 and M, inclusive.

Find the number, modulo 998244353, of sequences A = (A\_1, A\_2, \dots, A\_N) of length N consisting of integers between 1 and M, inclusive, that satisfy the following condition:

* For each B = 1, 2, \dots, M, the value X\_B exists between any two different occurrences of B in A (including both ends).

More formally, for each B = 1, 2, \dots, M, the following condition must hold:

* For every pair of integers (l, r) such that 1 \leq l < r \leq N and A\_l = A\_r = B, there exists an integer m (l \leq m \leq r) such that A\_m = X\_B.

### Constraints

* 1 \leq M \leq 10
* 1 \leq N \leq 10^4
* 1 \leq X\_i \leq M
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
M N
X_1 X_2 \cdots X_M
```

### Output

Print the answer.

---

### Sample Input 1

```
3 4
2 1 2
```

### Sample Output 1

```
14
```

Here are examples of sequences A that satisfy the condition:

* (1, 3, 2, 3)
* (2, 1, 2, 1)
* (3, 2, 1, 3)

Here are non-examples:

* (1, 3, 1, 3)
  + There is no X\_3 = 2 between the 3s.
* (2, 2, 1, 3)
  + There is no X\_2 = 1 between the 2s.

---

### Sample Input 2

```
4 8
1 2 3 4
```

### Sample Output 2

```
65536
```

All sequences of length 8 consisting of integers between 1 and 4 satisfy the condition.

Note that when X\_B = B, there is always a B between two different occurrences of B.

---

### Sample Input 3

```
4 9
2 3 4 1
```

### Sample Output 3

```
628
```
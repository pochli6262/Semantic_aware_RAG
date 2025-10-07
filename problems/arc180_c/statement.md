Score : 600 points

### Problem Statement

You are given an integer sequence A=(A\_1,A\_2,\cdots,A\_N) of length N.

You will perform the following operation exactly once:

* Choose a non-empty subsequence of A (not necessarily contiguous) and replace it with its cumulative sums.
  More precisely, first choose a sequence of indices (i\_1,i\_2,\cdots,i\_k) such that 1 \leq i\_1 < i\_2 < \cdots < i\_k \leq N.
  The length of the sequence k (1 \leq k \leq N) can be chosen freely.
  Then, for each j (1 \leq j \leq k), replace the value of A\_{i\_j} with \sum\_{1 \leq x \leq j} A\_{i\_x}.
  This replacement is done simultaneously for all chosen indices.

Find, modulo 10^9+7, the number of possible sequences A after the operation.

### Constraints

* 1 \leq N \leq 100
* -10 \leq A\_i \leq 10
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \cdots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
1 1 2
```

### Sample Output 1

```
4
```

The possible sequences A after the operation are as follows:

* A=(1,1,2): This can be achieved with k=1 and (i\_1)=(1).
* A=(1,2,2): This can be achieved with k=2 and (i\_1,i\_2)=(1,2).
* A=(1,1,3): This can be achieved with k=2 and (i\_1,i\_2)=(1,3).
* A=(1,2,4): This can be achieved with k=3 and (i\_1,i\_2,i\_3)=(1,2,3).

---

### Sample Input 2

```
4
1 -1 1 -1
```

### Sample Output 2

```
8
```

---

### Sample Input 3

```
5
0 0 0 0 0
```

### Sample Output 3

```
1
```

---

### Sample Input 4

```
40
2 -2 1 3 -3 -1 -2 -3 0 -1 -2 0 -3 0 0 2 0 -1 2 -2 -2 -1 3 -2 -2 -2 2 3 2 -3 0 -2 2 1 3 0 -1 0 -2 -3
```

### Sample Output 4

```
420429545
```
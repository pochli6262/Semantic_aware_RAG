Score : 300 points

### Problem Statement

You are given a permutation P = (P\_1, \dots, P\_N) of (1, \dots, N), where (P\_1, \dots, P\_N) \neq (1, \dots, N).

Assume that P is the K-th lexicographically smallest among all permutations of (1 \dots, N). Find the (K-1)-th lexicographically smallest permutation.

 What are permutations?

A **permutation** of (1, \dots, N) is an arrangement of (1, \dots, N) into a sequence.

 What is lexicographical order?

For sequences of length N, A = (A\_1, \dots, A\_N) and B = (B\_1, \dots, B\_N), A is said to be **strictly lexicographically smaller** than B if and only if there is an integer 1 \leq i \leq N that satisfies both of the following.

* (A\_{1},\ldots,A\_{i-1}) = (B\_1,\ldots,B\_{i-1}).
* A\_i < B\_i.

### Constraints

* 2 \leq N \leq 100
* 1 \leq P\_i \leq N \, (1 \leq i \leq N)
* P\_i \neq P\_j \, (i \neq j)
* (P\_1, \dots, P\_N) \neq (1, \dots, N)
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
P_1 \ldots P_N
```

### Output

Let Q = (Q\_1, \dots, Q\_N) be the sought permutation. Print Q\_1, \dots, Q\_N in a single line in this order, separated by spaces.

---

### Sample Input 1

```
3
3 1 2
```

### Sample Output 1

```
2 3 1
```

Here are the permutations of (1, 2, 3) in ascending lexicographical order.

* (1, 2, 3)
* (1, 3, 2)
* (2, 1, 3)
* (2, 3, 1)
* (3, 1, 2)
* (3, 2, 1)

Therefore, P = (3, 1, 2) is the fifth smallest, so the sought permutation, which is the fourth smallest (5 - 1 = 4), is (2, 3, 1).

---

### Sample Input 2

```
10
9 8 6 5 10 3 1 2 4 7
```

### Sample Output 2

```
9 8 6 5 10 2 7 4 3 1
```
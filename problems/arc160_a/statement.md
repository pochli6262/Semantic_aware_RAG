Score : 400 points

### Problem Statement

You are given a permutation A = (A\_1, A\_2, \dots, A\_N) of (1, 2, \dots, N).  
For a pair of integers (L, R) such that 1 \leq L \leq R \leq N, let f(L, R) be the permutation obtained by reversing the L-th through R-th elements of A, that is, replacing A\_L, A\_{L+1}, \dots, A\_{R-1}, A\_R with A\_R, A\_{R-1}, \dots, A\_{L+1}, A\_{L} simultaneously.

There are \frac{N(N + 1)}{2} ways to choose (L, R) such that 1 \leq L \leq R \leq N.  
If the permutations f(L, R) for all such pairs (L, R) are listed and sorted in lexicographical order, what is the K-th permutation from the front?

 What is lexicographical order on sequences?

A sequence S = (S\_1,S\_2,\ldots,S\_{|S|}) is said to be **lexicographically smaller** than a sequence T = (T\_1,T\_2,\ldots,T\_{|T|}) if and only if 1. or 2. below holds.
Here, |S| and |T| denote the lengths of S and T, respectively.

1. |S| \lt |T| and (S\_1,S\_2,\ldots,S\_{|S|}) = (T\_1,T\_2,\ldots,T\_{|S|}).
2. There is an integer 1 \leq i \leq \min\lbrace |S|, |T| \rbrace that satisfies both of the following.
   * (S\_1,S\_2,\ldots,S\_{i-1}) = (T\_1,T\_2,\ldots,T\_{i-1}).
   * S\_i is smaller than T\_i (as a number).

### Constraints

* 1 \leq N \leq 7000
* 1 \leq K \leq \frac{N(N + 1)}{2}
* A is a permutation of (1, 2, \dots, N).

---

### Input

The input is given from Standard Input in the following format:

```
N K
A_1 A_2 \dots A_N
```

### Output

Let B =(B\_1, B\_2, \dots, B\_N) be the K-th permutation from the front in the list of the permutations f(L, R) sorted in lexicographical order.  
Print B in the following format:

```
B_1 B_2 \dots B_N
```

---

### Sample Input 1

```
3 5
1 3 2
```

### Sample Output 1

```
2 3 1
```

Here are the permutations f(L, R) for all pairs (L, R) such that 1 \leq L \leq R \leq N.

* f(1, 1) = (1, 3, 2)
* f(1, 2) = (3, 1, 2)
* f(1, 3) = (2, 3, 1)
* f(2, 2) = (1, 3, 2)
* f(2, 3) = (1, 2, 3)
* f(3, 3) = (1, 3, 2)

When these are sorted in lexicographical order, the fifth permutation is f(1, 3) = (2, 3, 1), which should be printed.

---

### Sample Input 2

```
5 15
1 2 3 4 5
```

### Sample Output 2

```
5 4 3 2 1
```

The answer is f(1, 5).

---

### Sample Input 3

```
10 37
9 2 1 3 8 7 10 4 5 6
```

### Sample Output 3

```
9 2 1 6 5 4 10 7 8 3
```
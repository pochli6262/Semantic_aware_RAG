Score : 600 points

### Problem Statement

You are given a permutation P=(P\_1,P\_2,\dots,P\_N) of integers from 1 to N and an integer K.

Consider the following operation on the permutation P.

* Choose an integer i such that 1 \leq i \leq N-K+1, and sort P\_i,P\_{i+1},\dots,P\_{i+K-1} in ascending order. That is, let (x\_1,x\_2,\dots,x\_K) be the result of arranging P\_i,P\_{i+1},\dots,P\_{i+K-1} in order from smallest to largest, and replace P\_{i+j-1} with x\_j for each 1 \leq j \leq K.

Find the lexicographically largest permutation that can be obtained by performing the above operation on P exactly once.

 What is lexicographical order on sequences?

A sequence S = (S\_1,S\_2,\ldots,S\_{|S|}) is **lexicographically smaller** than T = (T\_1,T\_2,\ldots,T\_{|T|}) when 1. or 2. below holds.
Here, |S| and |T| denotes the lengths of S and T, respectively.

1. |S| \lt |T| and (S\_1,S\_2,\ldots,S\_{|S|}) = (T\_1,T\_2,\ldots,T\_{|S|}).
2. There is an integer 1 \leq i \leq \min\lbrace |S|, |T| \rbrace that satisfy both of the following:
   * (S\_1,S\_2,\ldots,S\_{i-1}) = (T\_1,T\_2,\ldots,T\_{i-1}).
   * S\_i is smaller than T\_i (as a number).

### Constraints

* 1 \leq K \leq N \leq 2 \times 10^5
* 1 \leq P\_i \leq N
* (P\_1,P\_2,\dots,P\_N) is a permutation of integers from 1 to N.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K
P_1 P_2 \dots P_N
```

### Output

Print the lexicographically largest permutation that can be obtained by performing the above operation on P exactly once, with spaces in between.

---

### Sample Input 1

```
4 3
2 1 4 3
```

### Sample Output 1

```
2 1 3 4
```

If you perform the operation with i=1, we have (P\_1,P\_2,P\_3)=(2,1,4), and sorting it in ascending order yields (1,2,4). Thus, the operation replaces P\_1,P\_2,P\_3 with 1,2,4, respectively, resulting in P=(1,2,4,3). Similarly, if you perform the operation with i=2, P becomes (2,1,3,4).

The lexicographically greater between them is (2,1,3,4), so the answer is (2,1,3,4).

---

### Sample Input 2

```
5 1
3 1 4 2 5
```

### Sample Output 2

```
3 1 4 2 5
```

---

### Sample Input 3

```
20 7
9 4 3 1 11 12 13 15 17 7 2 5 6 20 19 18 8 16 14 10
```

### Sample Output 3

```
9 4 3 1 11 12 13 15 17 7 2 5 6 8 18 19 20 16 14 10
```
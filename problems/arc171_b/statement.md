Score: 600 points

### Problem Statement

For a permutation P = (P\_1, P\_2, \dots, P\_N) of (1, 2, \dots, N), we define F(P) by the following procedure:

* There is a sequence B = (1, 2, \dots, N).  
  As long as there is an integer i such that B\_i \lt P\_{B\_i}, perform the following operation:
  + Let j be the smallest integer i that satisfies B\_i \lt P\_{B\_i}. Then, replace B\_j with P\_{B\_j}.Define F(P) as the B at the end of this process. (It can be proved that the process terminates after a finite number of steps.)

You are given a sequence A = (A\_1, A\_2, \dots, A\_N) of length N. How many permutations P of (1,2,\dots,N) satisfy F(P) = A? Find the count modulo 998244353.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq N
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

Print the number, modulo 998244353, of permutations P that satisfy F(P) = A.

---

### Sample Input 1

```
4
3 3 3 4
```

### Sample Output 1

```
1
```

For example, if P = (2, 3, 1, 4), then F(P) is determined to be (3, 3, 3, 4) by the following steps:

* Initially, B = (1, 2, 3, 4).
* The smallest integer i such that B\_i \lt P\_{B\_i} is 1. Replace B\_1 with P\_{B\_1} = 2, making B = (2, 2, 3, 4).
* The smallest integer i such that B\_i \lt P\_{B\_i} is 1. Replace B\_1 with P\_{B\_1} = 3, making B = (3, 2, 3, 4).
* The smallest integer i such that B\_i \lt P\_{B\_i} is 2. Replace B\_2 with P\_{B\_2} = 3, making B = (3, 3, 3, 4).
* There are no more i that satisfy B\_i \lt P\_{B\_i}, so the process ends. The current B = (3, 3, 3, 4) is defined as F(P).

There is only one permutation P such that F(P) = A, which is (2, 3, 1, 4).

---

### Sample Input 2

```
4
2 2 4 3
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
8
6 6 8 4 5 6 8 8
```

### Sample Output 3

```
18
```
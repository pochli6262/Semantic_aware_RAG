Score : 300 points

### Problem Statement

You are given a sequence A = (A\_1, A\_2, \ldots, A\_N) of length N.
For each K = 0, 1, 2, \ldots, N-1, solve the following problem.

> Find the number of integers i between 1 and N (inclusive) such that:
>
> * A contains exactly K distinct integers greater than A\_i.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
```

### Output

Print N lines.
For i = 1, 2, \ldots, N, the i-th line should contain the answer for K = i-1.

---

### Sample Input 1

```
6
2 7 1 8 2 8
```

### Sample Output 1

```
2
1
2
1
0
0
```

For example, we will find the answer for K=2.

* Regarding A\_1 = 2, A contains 2 distinct integers greater than A\_1: 7 and 8.
* Regarding A\_2 = 7, A contains 1 distinct integer greater than A\_2: 8.
* Regarding A\_3 = 1, A contains 3 distinct integers greater than A\_3: 2, 7, and 8.
* Regarding A\_4 = 8, A contains 0 distinct integers greater than A\_4 (there is no such integer).
* Regarding A\_5 = 2, A contains 2 distinct integers greater than A\_5: 7 and 8.
* Regarding A\_6 = 8, A contains 0 distinct integers greater than A\_6 (there is no such integer).

Thus, there are two i's, i = 1 and i = 5, such that A contains exactly K = 2 distinct integers greater than A\_i. Therefore, the answer for K = 2 is 2.

---

### Sample Input 2

```
1
1
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
10
979861204 57882493 979861204 447672230 644706927 710511029 763027379 710511029 447672230 136397527
```

### Sample Output 3

```
2
1
2
1
2
1
1
0
0
0
```
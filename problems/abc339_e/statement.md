Score: 525 points

### Problem Statement

You are given a sequence A = (A\_1, A\_2, \ldots, A\_N) of length N.

Find the maximum length of a subsequence of A such that the absolute difference between any two adjacent terms is at most D.

A subsequence of a sequence A is a sequence that can be obtained by deleting zero or more elements from A and arranging the remaining elements in their original order.

### Constraints

* 1 \leq N \leq 5 \times 10^5
* 0 \leq D \leq 5 \times 10^5
* 1 \leq A\_i \leq 5 \times 10^5
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N D
A_1 A_2 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2
3 5 1 2
```

### Sample Output 1

```
3
```

The subsequence (3, 1, 2) of A has absolute differences of at most 2 between adjacent terms.

---

### Sample Input 2

```
5 10
10 20 100 110 120
```

### Sample Output 2

```
3
```

---

### Sample Input 3

```
11 7
21 10 3 19 28 12 11 3 3 15 16
```

### Sample Output 3

```
6
```
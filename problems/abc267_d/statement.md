Score : 400 points

### Problem Statement

You are given an integer sequence A=(A\_1,A\_2,\dots,A\_N) of length N.

Find the maximum value of \displaystyle \sum\_{i=1}^{M} i \times B\_i for a (not necessarily contiguous) subsequence B=(B\_1,B\_2,\dots,B\_M) of length M of A.

### Notes

A **subsequence** of a number sequence is a sequence that is obtained by removing 0 or more elements from the original number sequence and concatenating the remaining elements without changing the order.

For example, (10,30) is a subsequence of (10,20,30), but (20,10) is not a subsequence of (10,20,30).

### Constraints

* 1 \le M \le N \le 2000
* - 2 \times 10^5 \le A\_i \le 2 \times 10^5
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2
5 4 -1 8
```

### Sample Output 1

```
21
```

When B=(A\_1,A\_4), we have \displaystyle \sum\_{i=1}^{M} i \times B\_i = 1 \times 5 + 2 \times 8 = 21. Since it is impossible to achieve 22 or a larger value, the solution is 21.

---

### Sample Input 2

```
10 4
-3 1 -4 1 -5 9 -2 6 -5 3
```

### Sample Output 2

```
54
```
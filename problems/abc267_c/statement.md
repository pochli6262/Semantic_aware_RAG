Score : 300 points

### Problem Statement

You are given an integer sequence A=(A\_1,A\_2,\dots,A\_N) of length N.

Find the maximum value of \displaystyle \sum\_{i=1}^{M} i \times B\_i for a contiguous subarray B=(B\_1,B\_2,\dots,B\_M) of A of length M.

### Notes

A **contiguous subarray** of a number sequence is a sequence that is obtained by removing 0 or more initial terms and 0 or more final terms from the original number sequence.

For example, (2, 3) and (1, 2, 3) are contiguous subarrays of (1, 2, 3, 4), but (1, 3) and (3,2,1) are not contiguous subarrays of (1, 2, 3, 4).

### Constraints

* 1 \le M \le N \le 2 \times 10^5
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
15
```

When B=(A\_3,A\_4), we have \displaystyle \sum\_{i=1}^{M} i \times B\_i = 1 \times (-1) + 2 \times 8 = 15. Since it is impossible to achieve 16 or a larger value, the solution is 15.

Note that you are not allowed to choose, for instance, B=(A\_1,A\_4).

---

### Sample Input 2

```
10 4
-3 1 -4 1 -5 9 -2 6 -5 3
```

### Sample Output 2

```
31
```
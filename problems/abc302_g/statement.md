Score : 625 points

### Problem Statement

You are given a sequence A=(A\_1,A\_2,\ldots,A\_N) of length N, consisting of integers between 1 and 4.

Takahashi may perform the following operation any number of times (possibly zero):

* choose a pair of integer (i,j) such that 1\leq i<j\leq N, and swap A\_i and A\_j.

Find the minimum number of operations required to make A non-decreasing.  
A sequence is said to be non-decreasing if and only if A\_i\leq A\_{i+1} for all 1\leq i\leq N-1.

### Constraints

* 2 \leq N \leq 2\times 10^5
* 1\leq A\_i \leq 4
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
```

### Output

Print the minimum number of operations required to make A non-decreasing in a single line.

---

### Sample Input 1

```
6
3 4 1 1 2 4
```

### Sample Output 1

```
3
```

One can make A non-decreasing with the following three operations:

* Choose (i,j)=(2,3) to swap A\_2 and A\_3, making A=(3,1,4,1,2,4).
* Choose (i,j)=(1,4) to swap A\_1 and A\_4, making A=(1,1,4,3,2,4).
* Choose (i,j)=(3,5) to swap A\_3 and A\_5, making A=(1,1,2,3,4,4).

This is the minimum number of operations because it is impossible to make A non-decreasing with two or fewer operations.  
Thus, 3 should be printed.

---

### Sample Input 2

```
4
2 3 4 1
```

### Sample Output 2

```
3
```
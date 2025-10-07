Score : 600 points

### Problem Statement

Given is a sequence A of N numbers.

There are 2^{N-1} ways to divide A into non-empty **contiguous** subsequences B\_1,B\_2,\ldots,B\_k. Find the value below for each of those ways, and print the sum, modulo 998244353, of those values.

* \prod\_{i=1}^{k} (\max(B\_i)-\min(B\_i))

Here, for a sequence B\_i=(B\_{i,1},B\_{i,2},\ldots,B\_{i,j}), \max(B\_i) and \min(B\_i) are defined to be the maximum and minimum values of an element of B\_i, respectively.

### Constraints

* 1 \leq N \leq 3 \times 10^5
* 1 \leq A\_i \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
```

### Output

Print the sum, modulo 998244353, of the values found.

---

### Sample Input 1

```
3
1 2 3
```

### Sample Output 1

```
2
```

There are 4 ways to divide A=(1,2,3) into non-empty contiguous subsequences, as follows.

* (1), (2), (3)
* (1), (2,3)
* (1,2), (3)
* (1,2,3)

\prod\_{i=1}^{k} (\max(B\_i)-\min(B\_i)) for these divisions are 0, 0, 0, 2, respectively. The sum of them, 2, should be printed.

---

### Sample Input 2

```
4
1 10 1 10
```

### Sample Output 2

```
90
```

---

### Sample Input 3

```
10
699498050 759726383 769395239 707559733 72435093 537050110 880264078 699299140 418322627 134917794
```

### Sample Output 3

```
877646588
```

Be sure to print the sum modulo 998244353.
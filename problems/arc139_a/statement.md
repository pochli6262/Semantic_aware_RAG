Score : 300 points

### Problem Statement

For a positive integer x, let \mathrm{ctz}(x) be the number of trailing zeros in the binary representation of x.  
For example, we have \mathrm{ctz}(8)=3 because the binary representation of 8 is `1000`, and \mathrm{ctz}(5)=0 because the binary representation of 5 is `101`.

You are given a sequence of non-negative integers T = (T\_1,T\_2,\dots,T\_N).  
Consider making a sequence of positive integers A = (A\_1, A\_2, \dots, A\_N) of your choice so that it satisfies the following conditions.

* A\_1 \lt A\_2 \lt \cdots \lt A\_{N-1} \lt A\_N holds. In other words, A is strictly increasing.
* \mathrm{ctz}(A\_i) = T\_i holds for every integer i such that 1 \leq i \leq N.

What is the minimum possible value of A\_N here?

### Constraints

* 1 \leq N \leq 10^5
* 0 \leq T\_i \leq 40
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
T_1 T_2 \dots T_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4
0 1 3 2
```

### Sample Output 1

```
12
```

For example, A\_1=3,A\_2=6,A\_3=8,A\_4=12 satisfy the conditions.  
A\_4 cannot be 11 or less, so the answer is 12.

---

### Sample Input 2

```
5
4 3 2 1 0
```

### Sample Output 2

```
31
```

---

### Sample Input 3

```
1
40
```

### Sample Output 3

```
1099511627776
```

Note that the answer may not fit into a 32-bit integer.

---

### Sample Input 4

```
8
2 0 2 2 0 4 2 4
```

### Sample Output 4

```
80
```
Score: 600 points

### Problem Statement

For a sequence X composed of a finite number of non-negative integers, we define \mathrm{mex}(X) as the smallest non-negative integer not in X. For example, \mathrm{mex}((0,0, 1,3)) = 2, \mathrm{mex}((1)) = 0, \mathrm{mex}(()) = 0.

You are given a sequence S=(S\_1,\ldots,S\_N) of length N where each element is 0 or 1.

Find the number, modulo 998244353, of sequences A=(A\_1,A\_2,\ldots,A\_N) of length N consisting of integers between 0 and M, inclusive, that satisfy the following condition:

* For each i (1\leq i\leq N), A\_i = \mathrm{mex}((A\_1,A\_2,\ldots,A\_{i-1})) if S\_i=1, and A\_i \neq \mathrm{mex}((A\_1,A\_2,\ldots,A\_{i-1})) if S\_i=0.

### Constraints

* 1 \leq N \leq 5000
* 0 \leq M \leq 10^9
* S\_i is 0 or 1.
* All input numbers are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
S_1 \ldots S_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2
1 0 0 1
```

### Sample Output 1

```
4
```

The following four sequences satisfy the conditions:

* (0,0,0,1)
* (0,0,2,1)
* (0,2,0,1)
* (0,2,2,1)

---

### Sample Input 2

```
10 1000000000
0 0 1 0 0 0 1 0 1 0
```

### Sample Output 2

```
587954969
```

Be sure to find the count modulo 998244353.
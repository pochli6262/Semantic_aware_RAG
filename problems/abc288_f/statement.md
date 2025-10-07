Score : 500 points

### Problem Statement

You are given a positive integer X with N digits in decimal representation. None of the digits of X is 0.  
For a subset S of \lbrace 1,2, \ldots, N-1 \rbrace , let f(S) be defined as follows.

> See the decimal representation of X as a string of length N, and decompose it into |S| + 1 strings by splitting it between the i-th and (i + 1)-th characters if and only if i \in S.  
> Then, see these |S| + 1 strings as integers in decimal representation, and let f(S) be the product of these |S| + 1 integers.

There are 2^{N-1} subsets of \lbrace 1,2, \ldots, N-1 \rbrace , including the empty set, which can be S. Find the sum of f(S) over all these S, modulo 998244353.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* X has N digits in decimal representation, none of which is 0.
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
X
```

### Output

Print the answer.

---

### Sample Input 1

```
3
234
```

### Sample Output 1

```
418
```

For S = \emptyset, we have f(S) = 234.  
For S = \lbrace 1 \rbrace, we have f(S) = 2 \times 34 = 68.  
For S = \lbrace 2 \rbrace, we have f(S) = 23 \times 4 = 92.  
For S = \lbrace 1, 2 \rbrace, we have f(S) = 2 \times 3 \times 4 = 24.  
Thus, you should print 234 + 68 + 92 + 24 = 418.

---

### Sample Input 2

```
4
5915
```

### Sample Output 2

```
17800
```

---

### Sample Input 3

```
9
998244353
```

### Sample Output 3

```
258280134
```
Score : 500 points

### Problem Statement

For a string T of length L consisting of `d` and `p`, let f(T) be T rotated 180 degrees. More formally, let f(T) be the string that satisfies the following conditions.

* f(T) is a string of length L consisting of `d` and `p`.
* For every integer i such that 1 \leq i \leq L, the i-th character of f(T) differs from the (L + 1 - i)-th character of T.

For instance, if T = `ddddd`, f(T) = `ppppp`; if T = `dpdppp`, f(T)= `dddpdp`.

You are given a string S of length N consisting of `d` and `p`.  
You may perform the following operation **zero or one** time.

* Choose a pair of integers (L, R) such that 1 \leq L \leq R \leq N, and let T be the substring formed by the L-th through R-th characters of S. Then, replace the L-th through R-th characters of S with f(T).

For instance, if S= `dpdpp` and (L,R)=(2,4), we have T= `pdp` and f(T)= `dpd`, so S becomes `ddpdp`.

Print the lexicographically smallest string that S can become.

What is lexicographical order?

A string S = S\_1S\_2\ldots S\_{|S|} is said to be **lexicographically smaller** than a string T = T\_1T\_2\ldots T\_{|T|} if one of the following 1. and 2. holds.
Here, |S| and |T| denote the lengths of S and T, respectively.

1. |S| \lt |T| and S\_1S\_2\ldots S\_{|S|} = T\_1T\_2\ldots T\_{|S|}.
2. There is an integer 1 \leq i \leq \min\lbrace |S|, |T| \rbrace that satisfies the following two conditions:
   * S\_1S\_2\ldots S\_{i-1} = T\_1T\_2\ldots T\_{i-1}.
   * S\_i is smaller than T\_i in alphabetical order.

### Constraints

* 1 \leq N \leq 5000
* S is a string of length N consisting of `d` and `p`.
* N is an integer.

---

### Input

The input is given from Standard Input in the following format:

```
N
S
```

### Output

Print the answer.

---

### Sample Input 1

```
6
dpdppd
```

### Sample Output 1

```
dddpdd
```

Let (L, R) = (2, 5). Then, we have T = `pdpp` and f(T) = `ddpd`, so S becomes `dddpdd`.  
This is the lexicographically smallest string that can be obtained, so print it.

---

### Sample Input 2

```
3
ddd
```

### Sample Output 2

```
ddd
```

It may be optimal to skip the operation.

---

### Sample Input 3

```
11
ddpdpdppddp
```

### Sample Output 3

```
ddddpdpdddp
```
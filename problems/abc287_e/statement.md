Score : 500 points

### Problem Statement

You are given N strings consisting of lowercase English letters. Let S\_i be the i-th (i = 1, 2, \dots, N) of them.

For two strings x and y, \mathrm{LCP}(x, y) is defined to be the maximum integer n that satisfies all of the following conditions:

* The lengths of x and y are both at least n.
* For all integers i between 1 and n, inclusive, the i-th character of x and that of y are equal.

Find the following value for all i = 1, 2, \dots, N:

* \displaystyle \max\_{i \neq j} \mathrm{LCP}(S\_i, S\_j)

### Constraints

* 2 \leq N \leq 5 \times 10^5
* N is an integer.
* S\_i is a string of length at least 1 consisting of lowercase English letters (i = 1, 2, \dots, N).
* The sum of lengths of S\_i is at most 5 \times 10^5.

---

### Input

The input is given from Standard Input in the following format:

```
N
S_1
S_2
\vdots
S_N
```

### Output

Print N lines. The i-th (i = 1, 2, \dots, N) line should contain \displaystyle \max\_{i \neq j} \mathrm{LCP}(S\_i, S\_j).

---

### Sample Input 1

```
3
abc
abb
aac
```

### Sample Output 1

```
2
2
1
```

\mathrm{LCP}(S\_1, S\_2) = 2, \mathrm{LCP}(S\_1, S\_3) = 1, and \mathrm{LCP}(S\_2, S\_3) = 1.

---

### Sample Input 2

```
11
abracadabra
bracadabra
racadabra
acadabra
cadabra
adabra
dabra
abra
bra
ra
a
```

### Sample Output 2

```
4
3
2
1
0
1
0
4
3
2
1
```
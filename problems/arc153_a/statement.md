Score : 300 points

### Problem Statement

A positive integer x is said to be a **beautiful integer** if and only if x is a 9-digit integer whose decimal notation S\_1\ldots S\_9 (S\_i is the i-th character) satisfies all of the following conditions:

* S\_1 is not `0`,
* S\_1 = S\_2,
* S\_5 = S\_6, and
* S\_7 = S\_9.

For instance, 998244353 and 333333333 are beautiful integers, while 111112222 is not, since S\_5 \neq S\_6.

You are given a positive integer N. Print the N-th smallest beautiful integer.

### Constraints

* N is a positive integer.
* There are at least N beautiful integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
```

### Output

Print the N-th smallest beautiful integer.

---

### Sample Input 1

```
3
```

### Sample Output 1

```
110000020
```

The beautiful integers in ascending order are 110000000, 110000010, 110000020, \ldots.

---

### Sample Input 2

```
882436
```

### Sample Output 2

```
998244353
```

---

### Sample Input 3

```
2023
```

### Sample Output 3

```
110200222
```
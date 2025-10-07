Score : 500 points

### Problem Statement

We have N cards. The i-th card has a string S\_i written on it.

Find the lexicographically smallest string that can be obtained by choosing K of these cards and concatenating them in any order.

### Constraints

* 1 \leq K \leq N \leq 50
* 1 \leq |S\_i| \leq 50
* S\_i consists of lowercase English letters.

---

### Input

Input is given from Standard Input in the following format:

```
N K
S_1
S_2
\vdots
S_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 3
ode
zaaa
r
atc
```

### Sample Output 1

```
atcoder
```

Note that it is not possible to reverse or permute the string written on a card.  
For example, `ode` written on the first card cannot be used as `edo` or `deo`.

---

### Sample Input 2

```
5 2
z
z
zzz
z
zzzzzz
```

### Sample Output 2

```
zz
```

There may be a pair i, j (i\neq j) such that S\_i = S\_j.
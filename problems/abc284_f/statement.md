Score : 500 points

### Problem Statement

For a string S of length N and an integer i\ (0\leq i\leq N), let us define the string f\_i(S) as the concatenation of:

* the first i characters of S,
* the reversal of S, and
* the last (N-i) characters of S,

in this order.
For instance, if S= `abc` and i=2, we have f\_i(S)= `abcbac`.

You are given a string T of length 2N.
Find a pair of a string S of length N and an integer i\ (0\leq i\leq N) such that f\_i(S)=T.
If no such pair of S and i exists, report that fact.

### Constraints

* 1\leq N \leq 10^6
* N is an integer.
* T is a string of length 2N consisting of lowercase English letters.

---

### Input

The input is given from Standard Input in the following format:

```
N 
T
```

### Output

If no pair of S and i satisfies the condition, print `-1`.
Otherwise, print S and i, separated by a newline.
If multiple pairs of S and i satisfy the condition, you may print any of them.

---

### Sample Input 1

```
3
abcbac
```

### Sample Output 1

```
abc
2
```

As mentioned in the problem statement, if S= `abc` and i=2, we have f\_i(S)= `abcbac`, which equals T, so you should print `abc` and 2.

---

### Sample Input 2

```
4
abababab
```

### Sample Output 2

```
abab
1
```

S= `abab` and i=3 also satisfy the condition.

---

### Sample Input 3

```
3
agccga
```

### Sample Output 3

```
cga
0
```

S= `agc` and i=3 also satisfy the condition.

---

### Sample Input 4

```
4
atcodeer
```

### Sample Output 4

```
-1
```

If no pair of S and i satisfies the condition, print `-1`.
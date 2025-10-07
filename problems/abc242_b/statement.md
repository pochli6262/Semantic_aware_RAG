Score : 200 points

### Problem Statement

You are given a string S. Find the lexicographically smallest string S' obtained by permuting the characters of S.

Here, for different two strings s = s\_1 s\_2 \ldots s\_n and t = t\_1 t\_2 \ldots t\_m, s \lt t holds lexicographically when one of the conditions below is satisfied.

* There is an integer i\ (1 \leq i \leq \min(n,m)) such that s\_i \lt t\_i and s\_j=t\_j for all integers j\ (1 \leq j \lt i).
* s\_i = t\_i for all integers i\ (1 \leq i \leq \min(n,m)), and n \lt m.

### Constraints

* S is a string of length between 1 and 2 \times 10^5 (inclusive) consisting of lowercase English letters.

---

### Input

Input is given from Standard Input in the following format:

```
S
```

### Output

Print the lexicographically smallest string S' obtained by permuting the characters in S.

---

### Sample Input 1

```
aba
```

### Sample Output 1

```
aab
```

Three strings can be obtained by permuting `aba`:

* `aba`
* `aab`
* `baa`

The lexicographically smallest among them is `aab`.

---

### Sample Input 2

```
zzzz
```

### Sample Output 2

```
zzzz
```
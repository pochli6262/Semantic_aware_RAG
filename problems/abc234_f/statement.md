Score : 500 points

### Problem Statement

Given is a string S. How many different strings can be obtained as a permutation of a non-empty, **not necessarily contiguous** subsequence of S?

Since the count can be enormous, print it modulo 998244353.

### Constraints

* S is a string of length 1 and 5000 (inclusive) consisting of lowercase English letters.

---

### Input

Input is given from Standard Input in the following format:

```
S
```

### Output

Print the number of different strings that can be obtained as a permutation of a subsequence of S, modulo 998244353.

---

### Sample Input 1

```
aab
```

### Sample Output 1

```
8
```

There are 8 different strings that can be obtained as a permutation of a subsequence of S: `a`, `b`, `aa`, `ab`, `ba`, `aab`, `aba`, `baa`.

---

### Sample Input 2

```
aaa
```

### Sample Output 2

```
3
```

---

### Sample Input 3

```
abcdefghijklmnopqrstuvwxyz
```

### Sample Output 3

```
149621752
```

Be sure to print the count modulo 998244353.
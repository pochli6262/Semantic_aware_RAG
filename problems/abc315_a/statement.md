Score : 100 points

### Problem Statement

You are given a string S consisting of lowercase English letters.  
Remove all occurrences of `a`, `e`, `i`, `o`, `u` from S and print the resulting string.  
S contains at least one character other than `a`, `e`, `i`, `o`, `u`.

### Constraints

* S is a string of length between 1 and 100, inclusive, consisting of lowercase English letters.
* S contains at least one character other than `a`, `e`, `i`, `o`, `u`.

---

### Input

The input is given from Standard Input in the following format:

```
S
```

### Output

Print the answer.

---

### Sample Input 1

```
atcoder
```

### Sample Output 1

```
tcdr
```

For S = `atcoder`, remove the 1-st, 4-th, and 6-th characters to get `tcdr`.

---

### Sample Input 2

```
xyz
```

### Sample Output 2

```
xyz
```

---

### Sample Input 3

```
aaaabbbbcccc
```

### Sample Output 3

```
bbbbcccc
```
Score: 150 points

### Problem Statement

You are given a string S consisting of lowercase English letters and `|`. S is guaranteed to contain exactly two `|`s.

Remove the characters between the two `|`s, including the `|`s themselves, and print the resulting string.

### Constraints

* S is a string of length between 2 and 100, inclusive, consisting of lowercase English letters and `|`.
* S contains exactly two `|`s.

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
atcoder|beginner|contest
```

### Sample Output 1

```
atcodercontest
```

Remove all the characters between the two `|`s and print the result.

---

### Sample Input 2

```
|spoiler|
```

### Sample Output 2

```

```

It is possible that all characters are removed.

---

### Sample Input 3

```
||xyz
```

### Sample Output 3

```
xyz
```
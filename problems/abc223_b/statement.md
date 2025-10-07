Score : 200 points

### Problem Statement

On a non-empty string, a **left shift** moves the first character to the end of the string, and a **right shift** moves the last character to the beginning of the string.

For example, a left shift on `abcde` results in `bcdea`, and two right shifts on `abcde` result in `deabc`.

You are given a non-empty S consisting of lowercase English letters. Among the strings that can be obtained by performing zero or more left shifts and zero or more right shifts on S, find the lexicographically smallest string and the lexicographically largest string.

What is the lexicographical order?

Simply speaking, the lexicographical order is the order in which words are listed in a dictionary. As a more formal definition, here is the algorithm to determine the lexicographical order between different strings S and T.

Below, let S\_i denote the i-th character of S. Also, if S is lexicographically smaller than T, we will denote that fact as S \lt T; if S is lexicographically larger than T, we will denote that fact as S \gt T.

1. Let L be the smaller of the lengths of S and T. For each i=1,2,\dots,L, we check whether S\_i and T\_i are the same.
2. If there is an i such that S\_i \neq T\_i, let j be the smallest such i. Then, we compare S\_j and T\_j. If S\_j comes earlier than T\_j in alphabetical order, we determine that S \lt T and quit; if S\_j comes later than T\_j, we determine that S \gt T and quit.
3. If there is no i such that S\_i \neq T\_i, we compare the lengths of S and T. If S is shorter than T, we determine that S \lt T and quit; if S is longer than T, we determine that S \gt T and quit.

### Constraints

* S consists of lowercase English letters.
* The length of S is between 1 and 1000 (inclusive).

---

### Input

Input is given from Standard Input in the following format:

```
S
```

### Output

Print two lines. The first line should contain S\_{\min}, and the second line should contain S\_{\max}. Here, S\_{\min} and S\_{\max} are respectively the lexicographically smallest and largest strings obtained by performing zero or more left shifts and zero or more right shifts on S.

---

### Sample Input 1

```
aaba
```

### Sample Output 1

```
aaab
baaa
```

By performing shifts, we can obtain four strings: `aaab`, `aaba`, `abaa`, `baaa`. The lexicographically smallest and largest among them are `aaab` and `baaa`, respectively.

---

### Sample Input 2

```
z
```

### Sample Output 2

```
z
z
```

Any sequence of operations results in `z`.

---

### Sample Input 3

```
abracadabra
```

### Sample Output 3

```
aabracadabr
racadabraab
```
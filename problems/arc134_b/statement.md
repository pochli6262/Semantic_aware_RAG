Score : 400 points

### Problem Statement

Given is a string s of length N.
Let s\_i denote the i-th character of s.

Snuke will transform s by the following procedure.

* Choose an **even length** (not necessarily contiguous) subsequence x=(x\_1, x\_2, \ldots, x\_{2k}) of (1,2, \ldots, N) (k may be 0).
* Swap s\_{x\_1} and s\_{x\_{2k}}.
* Swap s\_{x\_2} and s\_{x\_{2k-1}}.
* Swap s\_{x\_3} and s\_{x\_{2k-2}}.
* \vdots
* Swap s\_{x\_{k}} and s\_{x\_{k+1}}.

Among the strings that s can become after the procedure, find the lexicographically smallest one.

What is the lexicographical order?

Simply speaking, the lexicographical order is the order in which words are listed in a dictionary. As a more formal definition, here is the algorithm to determine the lexicographical order between different strings S and T.

Below, let S\_i denote the i-th character of S. Also, if S is lexicographically smaller than T, we will denote that fact as S \lt T; if S is lexicographically larger than T, we will denote that fact as S \gt T.

1. Let L be the smaller of the lengths of S and T. For each i=1,2,\dots,L, we check whether S\_i and T\_i are the same.
2. If there is an i such that S\_i \neq T\_i, let j be the smallest such i. Then, we compare S\_j and T\_j. If S\_j comes earlier than T\_j in alphabetical order, we determine that S \lt T and quit; if S\_j comes later than T\_j, we determine that S \gt T and quit.
3. If there is no i such that S\_i \neq T\_i, we compare the lengths of S and T. If S is shorter than T, we determine that S \lt T and quit; if S is longer than T, we determine that S \gt T and quit.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* s is a string of length N consisting of lowercase English letters.

---

### Input

Input is given from Standard Input in the following format:

```
N
s
```

### Output

Print the lexicographically smallest possible string s after the procedure by Snuke.

---

### Sample Input 1

```
4
dcab
```

### Sample Output 1

```
acdb
```

* When x=(1,3), the procedure just swaps s\_{1} and s\_{3}.
* The s after the procedure is `acdb`, the lexicographically smallest possible result.

---

### Sample Input 2

```
2
ab
```

### Sample Output 2

```
ab
```

* When x=(), the s after the procedure is `ab`, the lexicographically smallest possible result.
* Note that x may have a length of 0.

---

### Sample Input 3

```
16
cabaaabbbabcbaba
```

### Sample Output 3

```
aaaaaaabbbbcbbbc
```

---

### Sample Input 4

```
17
snwfpfwipeusiwkzo
```

### Sample Output 4

```
effwpnwipsusiwkzo
```
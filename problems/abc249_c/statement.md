Score : 300 points

### Problem Statement

You are given N strings S\_1,S\_2,\dots,S\_N consisting of lowercase English alphabets.

Consider choosing some number of strings from S\_1,S\_2,\dots,S\_N.

Find the maximum number of distinct alphabets that satisfy the following condition: "the alphabet is contained in exactly K of the chosen strings."

### Constraints

* 1 \le N \le 15
* 1 \le K \le N
* N and K are integers.
* S\_i is a non-empty string consisting of lowercase English alphabets.
* For each integer i such that 1 \le i \le N, S\_i does not contain two or more same alphabets.
* If i \neq j, then S\_i \neq S\_j.

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
4 2
abi
aef
bc
acg
```

### Sample Output 1

```
3
```

When S\_1,S\_3, and S\_4 are chosen, `a`,`b`, and `c` occur in exactly two of the strings.

There is no way to choose strings so that 4 or more alphabets occur in exactly 2 of the strings, so the answer is 3.

---

### Sample Input 2

```
2 2
a
b
```

### Sample Output 2

```
0
```

You cannot choose the same string more than once.

---

### Sample Input 3

```
5 2
abpqxyz
az
pq
bc
cy
```

### Sample Output 3

```
7
```
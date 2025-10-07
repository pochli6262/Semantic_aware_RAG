Score : 625 points

### Problem Statement

You are given N strings S\_1, S\_2, \ldots, S\_N consisting of lowercase English letters and N positive integers A\_1, A\_2, \ldots, A\_N.

A subset T of \lbrace 1, 2, \ldots, N \rbrace is called a **good set** if there is no pair i, j \in T (i \neq j) such that S\_i is a substring of S\_j.

Find the maximum possible value of \displaystyle \sum\_{i \in T} A\_i for a good set T.

What is a substring?
A **substring** of a string S is a string obtained by deleting zero or more characters from the beginning and zero or more characters from the end of S.
For example, `ab` is a substring of `abc`, but `ac` is not a substring of `abc`.

### Constraints

* 1 \leq N \leq 100
* S\_i is a string consisting of lowercase English letters.
* 1 \leq |S\_i|
* |S\_1| + |S\_2| + \ldots + |S\_N| \leq 5000
* 1 \leq A\_i \leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N
S_1
S_2
\vdots
S_N
A_1 A_2 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4
atcoder
at
coder
code
5 2 3 4
```

### Sample Output 1

```
6
```

The possible good sets T and their corresponding \displaystyle \sum\_{i \in T} A\_i are as follows:

* T = \lbrace 1 \rbrace: \displaystyle \sum\_{i \in T} A\_i = 5
* T = \lbrace 2 \rbrace: \displaystyle \sum\_{i \in T} A\_i = 2
* T = \lbrace 3 \rbrace: \displaystyle \sum\_{i \in T} A\_i = 3
* T = \lbrace 4 \rbrace: \displaystyle \sum\_{i \in T} A\_i = 4
* T = \lbrace 2, 3 \rbrace: \displaystyle \sum\_{i \in T} A\_i = 5
* T = \lbrace 2, 4 \rbrace: \displaystyle \sum\_{i \in T} A\_i = 6

The maximum among them is 6, so print 6.

---

### Sample Input 2

```
10
abcd
abc
ab
a
b
c
d
ab
bc
cd
100 10 50 30 60 90 80 70 40 20
```

### Sample Output 2

```
260
```
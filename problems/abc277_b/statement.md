Score : 200 points

### Problem Statement

You are given N strings, each of length 2, consisting of uppercase English letters and digits. The i-th string is S\_i.  
Determine whether the following three conditions are all satisfied.  
・For every string, the first character is one of `H`, `D`, `C`, and `S`.  
・For every string, the second character is one of `A`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `T`, `J`, `Q`, `K`.  
・All strings are pairwise different. That is, if i \neq j, then S\_i \neq S\_j.

### Constraints

* 1 \leq N \leq 52
* S\_i is a string of length 2 consisting of uppercase English letters and digits.

---

### Input

The input is given from Standard Input in the following format:

```
N
S_1
S_2
\vdots
S_N
```

### Output

If the three conditions are all satisfied, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
4
H3
DA
D3
SK
```

### Sample Output 1

```
Yes
```

One can verify that the three conditions are all satisfied.

---

### Sample Input 2

```
5
H3
DA
CK
H3
S7
```

### Sample Output 2

```
No
```

Both S\_1 and S\_4 are `H3`, violating the third condition.

---

### Sample Input 3

```
4
3H
AD
3D
KS
```

### Sample Output 3

```
No
```

---

### Sample Input 4

```
5
00
AA
XX
YY
ZZ
```

### Sample Output 4

```
No
```
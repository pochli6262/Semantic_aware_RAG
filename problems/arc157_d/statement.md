Score : 600 points

### Problem Statement

There is a grid with H rows and W columns where each square has one of the characters `X` and `Y` written on it.
Let (i, j) denote the square at the i-th row from the top and j-th column from the left.
The characters on the grid are given as H strings S\_1, S\_2, \dots, S\_H: the j-th character of S\_i is the character on square (i, j).

You can set up fences across the grid between adjacent rows and columns.
Fences may intersect.
After setting up fences, a **block** is defined as the set of squares reachable from some square by repeatedly moving up, down, left, or right to the adjacent square without crossing fences. (See also Sample Output 1.)

There are 2^{H-1} \times 2^{W-1} ways to set up fences. How many of them satisfy the following condition, modulo 998244353?

**Condition:** Each block has exactly two squares with `Y` written on it.

### Constraints

* 1 \leq H \leq 2000
* 1 \leq W \leq 2000
* S\_i \ (1 \leq i \leq H) is a string of length W consisting of `X` and `Y`.

---

### Input

The input is given from Standard Input in the following format:

```
H W
S_1
S_2
\vdots
S_H
```

### Output

Print the number of ways to set up fences to satisfy the condition, modulo 998244353.

---

### Sample Input 1

```
2 3
XYY
YXY
```

### Sample Output 1

```
2
```

Below are the eight ways to set up fences.

```
X Y Y    X|Y Y    X Y|Y    X|Y|Y
          |          |      | |
Y X Y    Y|X Y    Y X|Y    Y|X|Y


X Y Y    X|Y Y    X Y|Y    X|Y|Y
-----    -+---    ---+-    -+-+-
Y X Y    Y|X Y    Y X|Y    Y|X|Y
```

For instance, if a fence is set up between the 2-nd and 3-rd columns, the blocks are:

```
XY
YX
```

```
Y
Y
```

Each of these blocks has exactly two `Y`s, so the condition is satisfied.

If a fence is set up between the 1-st and 2-nd rows and the 1-st and 2-nd columns, the blocks are:

```
X
```

```
YY
```

```
Y
```

```
XY
```

These blocks, except the second, do not have exactly two `Y`s, so the condition is not satisfied.

---

### Sample Input 2

```
2 3
XYX
YYY
```

### Sample Output 2

```
0
```

There is no way to set up fences to satisfy the condition.

---

### Sample Input 3

```
2 58
YXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXY
YXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXY
```

### Sample Output 3

```
164036797
```

Print the number of ways modulo 998244353.
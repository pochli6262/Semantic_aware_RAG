Score : 600 points

### Problem Statement

We have an N \times N grid. The square at the i-th row from the top and j-th column from the left in this grid is called (i,j).  
Each square of the grid has at most one piece.  
The state of the grid is given by N strings S\_i:

* if the j-th character of S\_i is `O`, then (i,j) has a piece on it;
* if the j-th character of S\_i is `X`, then (i,j) has no piece on it.

You are given an integer M. Using this M, we define that a piece P placed at (s,t) covers a square (u,v) if all of the following conditions are satisfied:

* s \le u \le N
* t \le v \le N
* (u - s) + \frac{(v - t)}{2} < M

For each of Q squares (X\_i,Y\_i), find how many pieces cover the square.

### Constraints

* N, M, X\_i, Y\_i, and Q are integers.
* 1 \le N \le 2000
* 1 \le M \le 2 \times N
* S\_i consists of `O` and `X`.
* 1 \le Q \le 2 \times 10^5
* 1 \le X\_i,Y\_i \le N

---

### Input

Input is given from Standard Input in the following format:

```
N M
S_1
S_2
\vdots
S_N
Q
X_1 Y_1
X_2 Y_2
\vdots
X_Q Y_Q
```

### Output

Print Q lines.  
The i-th line ( 1 \le i \le Q ) should contain the number of pieces that covers (X\_i,Y\_i) as an integer.

---

### Sample Input 1

```
4 2
OXXX
XXXX
XXXX
XXXX
6
1 1
1 4
2 2
2 3
3 1
4 4
```

### Sample Output 1

```
1
1
1
0
0
0
```

Only Square (1,1) contains a piece, which covers the following `#` squares:

```
####
##..
....
....
```

---

### Sample Input 2

```
5 10
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
5
1 1
2 3
3 4
4 2
5 5
```

### Sample Output 2

```
1
6
12
8
25
```

---

### Sample Input 3

```
8 5
OXXOXXOX
XOXXOXOX
XOOXOOXO
OXOOXOXO
OXXOXXOX
XOXXOXOX
XOOXOOXO
OXOOXOXO
6
7 2
8 1
4 5
8 8
3 4
1 7
```

### Sample Output 3

```
5
3
9
14
5
3
```
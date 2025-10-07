Score : 600 points

### Problem Statement

We have a grid with N rows and M columns, where each square is painted black or white.
Here, at least one square is painted black.  
The initial state of the grid is given as N strings S\_1,S\_2,\ldots,S\_N of length M.  
The square at the i-th row from the top and j-th column from the left is painted black if the j-th character of S\_i is `#`, and white if it is `.`.

Takahashi wants to repaint some white squares (possibly zero) black so that the squares painted black are **connected**.
Find the minimum number of squares he needs to **repaint** to achieve his objective.

Here, the squares painted black are said to be **connected** when, for every pair of squares (S,T) painted black, there are a positive integer K and a sequence of K squares X=(x\_1,x\_2,\ldots,x\_K) painted black such that x\_1=S, x\_K=T, and x\_i and x\_{i+1} share a side for every 1\leq i\leq K-1.  
It can be proved that, under the constraints of the problem, there is always a way for Takahashi to achieve his objective.

### Constraints

* 1 \leq N \leq 100
* 1\leq M \leq 7
* N and M are integers.
* S\_i is a string of length M consisting of `#` and `.`.
* The given grid has at least one square painted black.

---

### Input

The input is given from Standard Input in the following format:

```
N M
S_1
S_2
\vdots
S_N
```

### Output

Print the minimum number of squares that Takahashi needs to repaint for the squares painted black to be connected.

---

### Sample Input 1

```
3 5
...#.
.#...
....#
```

### Sample Output 1

```
3
```

The initial grid looks as follows, where (i,j) denotes the square at the i-th row from the top and j-th column from the left.

![](https://img.atcoder.jp/abc296/d5b5d945798a02840b8add26271fe2a5.png)

Assume that Takahashi repaints three squares (2,3),(2,4),(3,4) (shown red in the figure below) black.

![](https://img.atcoder.jp/abc296/d2d0f1745af0dc309341f96dbd83e717.png)

Then, we have the following squares painted black, including the ones painted black from the beginning. These squares are connected.

![](https://img.atcoder.jp/abc296/76bebc05c2d7c5240151b534ba30f29b.png)

It is impossible to repaint two or fewer squares black so that the squares painted black are connected, so the answer is 3.  
Note that the squares painted white do not have to be connected.

---

### Sample Input 2

```
3 3
###
###
###
```

### Sample Output 2

```
0
```

All squares might be painted black from the beginning.

---

### Sample Input 3

```
10 1
.
#
.
.
.
.
.
.
#
.
```

### Sample Output 3

```
6
```
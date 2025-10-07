Score : 500 points

### Problem Statement

We have a grid with H rows from top to bottom and W columns from left and right. Initially, the square at the i-th row from the top and j-th column from the left has a lowercase English letter A\_{i,j}.

Let us perform Q operations on this grid. In the i-th operation, we are given integers a\_i and b\_i such that 1\leq a\_i \leq H-1 and 1\leq b\_i\leq W-1, and do the following.

* Let R\_1, R\_2, R\_3, and R\_4 be rectangular regions within the grid defined as follows:
  + R\_1 is the intersection of the top a\_i rows and leftmost b\_i columns;
  + R\_2 is the intersection of the top a\_i rows and rightmost W-b\_i columns;
  + R\_3 is the intersection of the bottom H-a\_i rows and leftmost b\_i columns;
  + R\_4 is the intersection of the bottom H-a\_i rows and rightmost W-b\_i columns.
* Rotate 180 degrees each of R\_1, R\_2, R\_3, and R\_4.

Here, a 180-degree rotation of a rectangular region R within the grid moves the character on the square at the i-th from the top and j-th column from the left in R to the square at the i-th from the bottom and j-th column from the right in R. See also the figures for the samples.

Print the grid after all Q operations.

### Constraints

* 2\leq H, W, and HW \leq 5\times 10^5.
* A\_{i,j} is a lowercase English letter.
* 1\leq Q\leq 2\times 10^5
* 1\leq a\_i\leq H - 1
* 1\leq b\_i\leq W - 1

---

### Input

The input is given from Standard Input in the following format:

```
H W
A_{1,1}\cdots A_{1, W}
\vdots
A_{H,1}\cdots A_{H, W}
Q
a_1 b_1
\vdots
a_Q b_Q
```

### Output

Print the grid after the operations in the following format, where B\_{i,j} is the character on the square (i,j) on the final grid.

```
B_{1,1}\cdots B_{1, W}
\vdots
B_{H,1}\cdots B_{H, W}
```

---

### Sample Input 1

```
4 5
abcde
fghij
klmno
pqrst
1
3 3
```

### Sample Output 1

```
mlkon
hgfji
cbaed
rqpts
```

The grid will change as follows.

![](https://img.atcoder.jp/arc153/5503f0a5f92e488238556b943aa1d6b7.png)

---

### Sample Input 2

```
3 7
atcoder
regular
contest
2
1 1
2 5
```

### Sample Output 2

```
testcon
oderatc
ularreg
```

The grid will change as follows.

![](https://img.atcoder.jp/arc153/353f0b30a9561e38967fb3aedf5767c5.png)

---

### Sample Input 3

```
2 2
ac
wa
3
1 1
1 1
1 1
```

### Sample Output 3

```
ac
wa
```

The grid will change as follows.

![](https://img.atcoder.jp/arc153/655a0ac98f0625e806f6abc97853a437.png)
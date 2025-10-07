Score : 300 points

### Problem Statement

Takahashi has two sheets A and B, each composed of black squares and transparent squares, and an infinitely large sheet C composed of transparent squares.  
There is also an ideal sheet X for Takahashi composed of black squares and transparent squares.

The sizes of sheets A, B, and X are H\_A rows \times W\_A columns, H\_B rows \times W\_B columns, and H\_X rows \times W\_X columns, respectively.  
The squares of sheet A are represented by H\_A strings of length W\_A, A\_1, A\_2, \ldots, A\_{H\_A} consisting of `.` and `#`.  
If the j-th character (1\leq j\leq W\_A) of A\_i (1\leq i\leq H\_A) is `.`, the square at the i-th row from the top and j-th column from the left is transparent; if it is `#`, that square is black.  
Similarly, the squares of sheets B and X are represented by H\_B strings of length W\_B, B\_1, B\_2, \ldots, B\_{H\_B}, and H\_X strings of length W\_X, X\_1, X\_2, \ldots, X\_{H\_X}, respectively.

Takahashi's goal is to create sheet X using **all black squares** in sheets A and B by following the steps below with sheets A, B, and C.

1. Paste sheets A and B onto sheet C along the grid. Each sheet can be pasted anywhere by translating it, but it cannot be cut or rotated.
2. Cut out an H\_X\times W\_X area from sheet C along the grid. Here, a square of the cut-out sheet will be black if a black square of sheet A or B is pasted there, and transparent otherwise.

Determine whether Takahashi can achieve his goal by appropriately choosing the positions where the sheets are pasted and the area to cut out, that is, whether he can satisfy both of the following conditions.

* The cut-out sheet includes **all black squares** of sheets A and B. The black squares of sheets A and B may overlap on the cut-out sheet.
* The cut-out sheet coincides sheet X without rotating or flipping.

### Constraints

* 1\leq H\_A, W\_A, H\_B, W\_B, H\_X, W\_X\leq 10
* H\_A, W\_A, H\_B, W\_B, H\_X, W\_X are integers.
* A\_i is a string of length W\_A consisting of `.` and `#`.
* B\_i is a string of length W\_B consisting of `.` and `#`.
* X\_i is a string of length W\_X consisting of `.` and `#`.
* Sheets A, B, and X each contain at least one black square.

---

### Input

The input is given from Standard Input in the following format:

```
H_A W_A
A_1
A_2
\vdots
A_{H_A}
H_B W_B
B_1
B_2
\vdots
B_{H_B}
H_X W_X
X_1
X_2
\vdots
X_{H_X}
```

### Output

If Takahashi can achieve the goal described in the problem statement, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3 5
#.#..
.....
.#...
2 2
#.
.#
5 3
...
#.#
.#.
.#.
...
```

### Sample Output 1

```
Yes
```

First, paste sheet A onto sheet C, as shown in the figure below.

```
     \vdots
  .......  
  .#.#...  
\cdots.......\cdots
  ..#....  
  .......  
     \vdots
```

Next, paste sheet B so that its top-left corner aligns with that of sheet A, as shown in the figure below.

```
     \vdots
  .......  
  .#.#...  
\cdots..#....\cdots
  ..#....  
  .......  
     \vdots
```

Now, cut out a 5\times 3 area with the square in the first row and second column of the range illustrated above as the top-left corner, as shown in the figure below.

```
...
#.#
.#.
.#.
...
```

This includes all black squares of sheets A and B and matches sheet X, satisfying the conditions.

Therefore, print `Yes`.

---

### Sample Input 2

```
2 2
#.
.#
2 2
#.
.#
2 2
##
##
```

### Sample Output 2

```
No
```

Note that sheets A and B may not be rotated or flipped when pasting them.

---

### Sample Input 3

```
1 1
#
1 2
##
1 1
#
```

### Sample Output 3

```
No
```

No matter how you paste or cut, you cannot cut out a sheet that includes all black squares of sheet B, so you cannot satisfy the first condition.
Therefore, print `No`.

---

### Sample Input 4

```
3 3
###
...
...
3 3
#..
#..
#..
3 3
..#
..#
###
```

### Sample Output 4

```
Yes
```
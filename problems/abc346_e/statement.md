Score: 450 points

### Problem Statement

There is a grid with H rows and W columns. Initially, all cells are painted with color 0.

You will perform the following operations in the order i = 1, 2, \ldots, M.

* If T\_i = 1, repaint all cells in the A\_i-th **row** with color X\_i.
* If T\_i = 2, repaint all cells in the A\_i-th **column** with color X\_i.

After all operations are completed, for each color i that exists on the grid, find the number of cells that are painted with color i.

### Constraints

* 1 \leq H, W, M \leq 2 \times 10^5
* T\_i \in \lbrace 1, 2 \rbrace
* 1 \leq A\_i \leq H for each i such that T\_i = 1,
* 1 \leq A\_i \leq W for each i such that T\_i = 2.
* 0 \leq X\_i \leq 2 \times 10^5
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
H W M
T_1 A_1 X_1
T_2 A_2 X_2
\vdots
T_M A_M X_M
```

### Output

Let K be the number of distinct integers i such that there are cells painted with color i. Print K + 1 lines.

The first line should contain the value of K.

The second and subsequent lines should contain, for each color i that exists on the grid, the color number i and the number of cells painted with that color.

Specifically, the (i + 1)-th line (1 \leq i \leq K) should contain the color number c\_i and the number of cells x\_i painted with color c\_i, in this order, separated by a space.

Here, print the color numbers **in ascending order**. That is, ensure that c\_1 < c\_2 < \ldots < c\_K. Note also that x\_i > 0 is required.

---

### Sample Input 1

```
3 4 4
1 2 5
2 4 0
1 3 3
1 3 2
```

### Sample Output 1

```
3
0 5
2 4
5 3
```

The operations will change the colors of the cells in the grid as follows:

```
0000   0000   0000   0000   0000
0000 → 5555 → 5550 → 5550 → 5550 
0000   0000   0000   3333   2222
```

Eventually, there are five cells painted with color 0, four with color 2, and three with color 5.

---

### Sample Input 2

```
1 1 5
1 1 1
1 1 10
2 1 100
1 1 1000
2 1 10000
```

### Sample Output 2

```
1
10000 1
```

---

### Sample Input 3

```
5 5 10
1 1 1
1 2 2
1 3 3
1 4 4
1 5 5
2 1 6
2 2 7
2 3 8
2 4 9
2 5 10
```

### Sample Output 3

```
5
6 5
7 5
8 5
9 5
10 5
```
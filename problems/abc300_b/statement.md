Score : 200 points

### Problem Statement

> Takahashi is developing an RPG. He has decided to write a code that checks whether two maps are equal.

We have grids A and B with H horizontal rows and W vertical columns. Each cell in the grid has a symbol `#` or `.` written on it.  
The symbols written on the cell at the i-th row from the top and j-th column from the left in A and B are denoted by A\_{i, j} and B\_{i, j}, respectively.

The following two operations are called a **vertical shift** and **horizontal shift**.

* For each j=1, 2, \dots, W, simultaneously do the following:
  + simultaneously replace A\_{1,j}, A\_{2,j}, \dots, A\_{H-1, j}, A\_{H,j} with A\_{2,j}, A\_{3,j}, \dots, A\_{H,j}, A\_{1,j}.
* For each i = 1, 2, \dots, H, simultaneously do the following:
  + simultaneously replace A\_{i,1}, A\_{i,2}, \dots, A\_{i,W-1}, A\_{i,W} with A\_{i, 2}, A\_{i, 3}, \dots, A\_{i,W}, A\_{i,1}.

Is there a pair of non-negative integers (s, t) that satisfies the following condition? Print `Yes` if there is, and `No` otherwise.

* After applying a vertical shift s times and a horizontal shift t times, A is equal to B.

Here, A is said to be equal to B if and only if A\_{i, j} = B\_{i, j} for all integer pairs (i, j) such that 1 \leq i \leq H and 1 \leq j \leq W.

### Constraints

* 2 \leq H, W \leq 30
* A\_{i,j} is `#` or `.`, and so is B\_{i,j}.
* H and W are integers.

---

### Input

The input is given from Standard Input in the following format:

```
H W
A_{1,1}A_{1,2}\dots A_{1,W}
A_{2,1}A_{2,2}\dots A_{2,W}
\vdots
A_{H,1}A_{H,2}\dots A_{H,W}
B_{1,1}B_{1,2}\dots B_{1,W}
B_{2,1}B_{2,2}\dots B_{2,W}
\vdots
B_{H,1}B_{H,2}\dots B_{H,W}
```

### Output

Print `Yes` if there is a conforming integer pair (s, t); print `No` otherwise.

---

### Sample Input 1

```
4 3
..#
...
.#.
...
#..
...
.#.
...
```

### Sample Output 1

```
Yes
```

By choosing (s, t) = (2, 1), the resulting A is equal to B.  
We describe the procedure when (s, t) = (2, 1) is chosen. Initially, A is as follows.

```
..#
...
.#.
...
```

We first apply a vertical shift to make A as follows.

```
...
.#.
...
..#
```

Then we apply another vertical shift to make A as follows.

```
.#.
...
..#
...
```

Finally, we apply a horizontal shift to make A as follows, which equals B.

```
#..
...
.#.
...
```

---

### Sample Input 2

```
3 2
##
##
#.
..
#.
#.
```

### Sample Output 2

```
No
```

No choice of (s, t) makes A equal B.

---

### Sample Input 3

```
4 5
#####
.#...
.##..
..##.
...##
#...#
#####
...#.
```

### Sample Output 3

```
Yes
```

---

### Sample Input 4

```
10 30
..........##########..........
..........####....###.....##..
.....##....##......##...#####.
....####...##..#####...##...##
...##..##..##......##..##....#
#.##....##....##...##..##.....
..##....##.##..#####...##...##
..###..###..............##.##.
.#..####..#..............###..
#..........##.................
................#..........##.
######....................####
....###.....##............####
.....##...#####......##....##.
.#####...##...##....####...##.
.....##..##....#...##..##..##.
##...##..##.....#.##....##....
.#####...##...##..##....##.##.
..........##.##...###..###....
...........###...#..####..#...
```

### Sample Output 4

```
Yes
```
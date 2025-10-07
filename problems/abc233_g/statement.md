Score : 600 points

### Problem Statement

There is a N \times N grid, with blocks on some squares.  
The grid is described by N strings S\_1,S\_2,\dots,S\_N, as follows.

* If the j-th character of S\_i is `#`, there is a block on the square at the i-th row from the top and j-th column from the left.
* If the j-th character of S\_i is `.`, there is not a block on the square at the i-th row from the top and j-th column from the left.

Takahashi can do the operation below zero or more times.

* First, choose an integer D between 1 and N (inclusive), and a D \times D subsquare within the grid.
* Then, consume D stamina points to destroy all blocks within the subsquare.

Find the minimum number of stamina points needed to destroy all the blocks.

### Constraints

* N is an integer.
* 1 \le N \le 50
* S\_i consists of `#` and `.`.
* |S\_i|=N

---

### Input

Input is given from Standard Input in the following format:

```
N
S_1
S_2
\vdots
S_N
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
5
##...
.##..
#.#..
.....
....#
```

### Sample Output 1

```
4
```

By choosing the subsquares below, Takahashi will consume 4 stamina points, which is optimal.

* The 3 \times 3 subsquare whose top-left square is at the 1-st row from the top and 1-st column from the left.
* The 1 \times 1 subsquare whose top-left square is at the 5-th row from the top and 5-th column from the left.

---

### Sample Input 2

```
3
...
...
...
```

### Sample Output 2

```
0
```

There may be no block on the grid.

---

### Sample Input 3

```
21
.....................
.....................
...#.#...............
....#.............#..
...#.#...........#.#.
..................#..
.....................
.....................
.....................
..........#.....#....
......#..###.........
........#####..#.....
.......#######.......
.....#..#####........
.......#######.......
......#########......
.......#######..#....
......#########......
..#..###########.....
.........###.........
.........###.........
```

### Sample Output 3

```
19
```
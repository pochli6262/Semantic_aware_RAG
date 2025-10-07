Score : 600 points

### Problem Statement

There is a grid with H \times W squares. Let (i,j) denote the square at the i-th row from the top and j-th column from the left.  
C\_{i,j} represents the state of each square. Each square is in one of the following four states.

* `S`: The starting point. The grid has exactly one starting point.
* `G`: The goal. The grid has exactly one goal.
* `.`: A constructible square, where a wall can be built.
* `O`: An unconstructible square, where a wall cannot be built.

Aoki intends to start at the starting point and get to the goal. When he is at (i,j), he can go to (i+1,j), (i,j+1), (i-1,j), or (i,j-1). It is not allowed to exit the grid or enter a square with a wall.

Takahashi decides to build a wall on one or more constructible squares of his choice before Aoki starts so that there is no way for Aoki to reach the goal. Here, the starting point and the goal cannot be chosen.

Is it possible for Takahashi to build walls to prevent Aoki from reaching the goal? If it is possible, also compute the two values below:

* the minimum number n of walls needed to prevent Aoki from reaching the goal, and
* the number of ways modulo 998244353, r, to achieve that minimum number of walls.

### Constraints

* 2 \leq H \leq 100
* 2 \leq W \leq 100
* C\_{i,j} is `S`, `G`, `.`, or `O`.
* Each of `S` and `G` appears exactly once in C\_{i,j}.

---

### Input

Input is given from Standard Input in the following format:

```
H W
C_{1,1}C_{1,2}\dotsC_{1,W}
C_{2,1}C_{2,2}\dotsC_{2,W}
\vdots
C_{H,1}C_{H,2}\dotsC_{H,W}
```

### Output

If it is possible to build walls to prevent Aoki from reaching the goal, print the string `Yes` and the integers n and r defined in the Problem Statement, in the following format:

```
Yes
n r
```

Otherwise, print `No`.

---

### Sample Input 1

```
4 3
S..
O..
..O
..G
```

### Sample Output 1

```
Yes
3 6
```

Let `#` represent a square to build a wall on. The six ways to achieve the minimum number of walls are as follows:

```
S#.  S.#  S..  S..  S..  S..
O#.  O#.  O##  O.#  O.#  O.#
#.O  #.O  #.O  ##O  .#O  .#O
..G  ..G  ..G  ..G  #.G  .#G
```

---

### Sample Input 2

```
3 2
.G
.O
.S
```

### Sample Output 2

```
No
```

Regardless of how Takahashi builds walls, Aoki can always reach the goal.

---

### Sample Input 3

```
2 2
S.
.G
```

### Sample Output 3

```
Yes
2 1
```

---

### Sample Input 4

```
10 10
OOO...OOO.
.....OOO.O
OOO.OO.OOO
OOO..O..S.
....O.O.O.
.OO.O.OOOO
..OOOG.O.O
.O.O..OOOO
.O.O.OO...
...O..O..O
```

### Sample Output 4

```
Yes
10 12
```
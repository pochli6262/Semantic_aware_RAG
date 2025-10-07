Score : 500 points

### Problem Statement

There is a skating rink represented by a grid with H horizontal rows and W vertical columns. Let (i, j) denote the square at the i-th row from the top and j-th column from the left.

The skating rink has N obstacles. The i-th obstacle is placed at (X\_i,Y\_i).

In a single move, Takahashi chooses one of the four directions, up, down, left, or right, and keeps moving until he hits an obstacle.  
When he hits an obstacle, he stops at the square right before the obstacle.
Since the skating rink is surrounded by cliffs, it is prohibited to start a move in which he will never hit an obstacle.

Takahashi is initially at (s\_x,s\_y). He wants to make some number of moves to stop at (g\_x,g\_y).

Find the minimum number of moves required to end up at (g\_x, g\_y). If it is not possible, report the fact.

### Constraints

* 1\leq H \leq 10^9
* 1\leq W \leq 10^9
* 1\leq N \leq 10^5
* 1\leq s\_x,g\_x\leq H
* 1\leq s\_y,g\_y\leq W
* 1\leq X\_i \leq H
* 1\leq Y\_i \leq W
* (s\_x,s\_y)\neq (g\_x,g\_y)
* (s\_x,s\_y)\neq (X\_i,Y\_i)
* (g\_x,g\_y)\neq (X\_i,Y\_i)
* If i\neq j, then (X\_i,Y\_i)\neq (X\_j,Y\_j).
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
H W N
s_x s_y
g_x g_y
X_1 Y_1
X_2 Y_2
\vdots
X_N Y_N
```

### Output

Print the minimum number of moves required to end up at (g\_x,g\_y).  
If it is impossible to end up there, print `-1`.

---

### Sample Input 1

```
7 8 7
3 4
5 6
1 4
2 1
2 8
4 5
5 7
6 2
6 6
```

### Sample Output 1

```
4
```

![](https://img.atcoder.jp/ghi/c376ca3813eb4c947eb605dea2d30454.png)

In the figure, (s\_x,s\_y) is denoted by `S` and (g\_x,g\_y) is denoted by `G`.  
By moving as (3,4)\rightarrow(2,4) \rightarrow(2,2) \rightarrow(5,2) \rightarrow(5,6), he can end up at (g\_x,g\_y) with 4 moves.

---

### Sample Input 2

```
4 6 2
3 2
3 5
4 5
2 5
```

### Sample Output 2

```
-1
```

![](https://img.atcoder.jp/ghi/07ab8a3e7c94525cd52704dd43e43b87.png)

He must stop at (g\_x,g\_y).  
Note that just passing through (g\_x,g\_y) is not considered to be ending up at the goal.

---

### Sample Input 3

```
1 10 1
1 5
1 1
1 7
```

### Sample Output 3

```
-1
```

![](https://img.atcoder.jp/ghi/a423524262f4a075b94e2ab5f9e61164.png)  
If he chooses to move to the left, Takahashi will fall down the cliff after passing through (g\_x,g\_y).  
Note that it is prohibited to start a move in which he will never hit an obstacle, as the skating rink is surrounded by cliffs.
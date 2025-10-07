Score : 600 points

### Problem Statement

Takahashi is in the square (0, 0, 0) in an infinite three-dimensional grid.

He can teleport between squares.
From the square (x, y, z), he can move to (x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), or (x, y, z-1) in one teleport. (Note that he cannot stay in the square (x, y, z).)

Find the number of routes ending in the square (X, Y, Z) after exactly N teleports.

In other words, find the number of sequences of N+1 triples of integers \big( (x\_0, y\_0, z\_0), (x\_1, y\_1, z\_1), (x\_2, y\_2, z\_2), \ldots, (x\_N, y\_N, z\_N)\big) that satisfy all three conditions below.

* (x\_0, y\_0, z\_0) = (0, 0, 0).
* (x\_N, y\_N, z\_N) = (X, Y, Z).
* |x\_i-x\_{i-1}| + |y\_i-y\_{i-1}| + |z\_i-z\_{i-1}| = 1 for each i = 1, 2, \ldots, N.

Since the number can be enormous, print it modulo 998244353.

### Constraints

* 1 \leq N \leq 10^7
* -10^7 \leq X, Y, Z \leq 10^7
* N, X, Y, and Z are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N X Y Z
```

### Output

Print the number modulo 998244353.

---

### Sample Input 1

```
3 2 0 -1
```

### Sample Output 1

```
3
```

There are three routes ending in the square (2, 0, -1) after exactly 3 teleports:

* (0, 0, 0) \rightarrow (1, 0, 0) \rightarrow (2, 0, 0) \rightarrow(2, 0, -1)
* (0, 0, 0) \rightarrow (1, 0, 0) \rightarrow (1, 0, -1) \rightarrow(2, 0, -1)
* (0, 0, 0) \rightarrow (0, 0, -1) \rightarrow (1, 0, -1) \rightarrow(2, 0, -1)

---

### Sample Input 2

```
1 0 0 0
```

### Sample Output 2

```
0
```

Note that exactly N teleports should be performed, and they do not allow him to stay in the same position.

---

### Sample Input 3

```
314 15 92 65
```

### Sample Output 3

```
106580952
```

Be sure to print the number modulo 998244353.
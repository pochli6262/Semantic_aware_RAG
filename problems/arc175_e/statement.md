Score: 800 points

### Problem Statement

> Divide a cube with a side length of N into N^3 smaller cubes, each with a side length of 1, and select K of these smaller cubes.
> Construct one way to select them so that, when viewed from any of the three directions perpendicular to the faces of the cubes, all K selected cubes are visible and appear in the same shape.

To formulate the problem precisely, we associate each smaller cube after division with a triple of integers (x\_i, y\_i, z\_i).

Construct and print one set of K triples of integers (x\_i, y\_i, z\_i) that satisfy the following conditions.

* 0 \leq x\_i, y\_i, z\_i < N
* \left\lbrace (x\_i, y\_i) \, \middle| \, 1 \le i \le K \right\rbrace = \left\lbrace (y\_i, z\_i) \, \middle| \, 1 \le i \le K \right\rbrace = \left\lbrace (z\_i, x\_i) \, \middle| \, 1 \le i \le K \right\rbrace
* The set mentioned in the previous item has K elements. That is, (x\_i, y\_i) \neq (x\_j, y\_j) for i \neq j.

It can be shown that a solution exists for any input satisfying the constraints.

### Constraints

* All input values are integers.
* 1 \leq N \leq 500
* 1 \leq K \leq N^2

---

### Input

The input is given from Standard Input in the following format:

```
N K
```

### Output

Print your answer in the following format:

```
x_1 y_1 z_1
x_2 y_2 z_2
\vdots
x_K y_K z_K
```

If multiple solutions exist, any of them will be accepted.

---

### Sample Input 1

```
3 3
```

### Sample Output 1

```
0 0 0
1 1 1
2 2 2
```

---

### Sample Input 2

```
2 4
```

### Sample Output 2

```
0 0 1
0 1 0
1 0 0
1 1 1
```

---

### Sample Input 3

```
1 1
```

### Sample Output 3

```
0 0 0
```
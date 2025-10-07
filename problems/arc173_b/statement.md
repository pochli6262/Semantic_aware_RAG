Score: 500 points

### Problem Statement

There are N distinct points on a two-dimensional plane. The coordinates of the i-th point are (x\_i,y\_i).

We want to create as many (non-degenerate) triangles as possible using these points as the vertices. Here, the same point cannot be used as a vertex of multiple triangles.

Find the maximum number of triangles that can be created.

What is a non-degenerate triangle?
A non-degenerate triangle is a triangle whose three vertices are not collinear.

### Constraints

* 3 \leq N \leq 300
* -10^9 \leq x\_i,y\_i \leq 10^9
* If i \neq j, then (x\_i,y\_i) \neq (x\_j,y\_j)
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
x_1 y_1
x_2 y_2
\vdots
x_{N} y_{N}
```

### Output

Print the answer.

---

### Sample Input 1

```
7
0 0
1 1
0 3
5 2
3 4
2 0
2 2
```

### Sample Output 1

```
2
```

For example, if we create a triangle from the first, third, and sixth points and another from the second, fourth, and fifth points, we can create two triangles.

The same point cannot be used as a vertex for multiple triangles, but the triangles may have overlapping areas.

---

### Sample Input 2

```
3
0 0
0 1000000000
0 -1000000000
```

### Sample Output 2

```
0
```
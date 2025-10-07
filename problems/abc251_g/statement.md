Score : 600 points

### Problem Statement

The vertices of a convex N-gon P in an xy-plane are given as (x\_1, y\_1), (x\_2, y\_2), \ldots, (x\_N, y\_N) in the **counterclockwise** order. (Here, the positive direction of the x-axis is right, and the positive direction of the y-axis is up.)

Based on this polygon P, we consider M convex N-gons P\_1, P\_2, \ldots, P\_M.  
For i = 1, 2, \ldots, M, the polygon P\_i is obtained by shifting P in the positive direction of the x-axis by u\_i and in the positive direction of the y-axis by v\_i. In other words, P\_i is a convex N-gon whose vertices are (x\_1+u\_i, y\_1+v\_i), (x\_2+u\_i, y\_2+v\_i), \ldots, (x\_N+u\_i, y\_N+v\_i).

For each of Q points (a\_1, b\_1), (a\_2, b\_2), \ldots, (a\_Q, b\_Q),
determine if "the point is contained in all of the M polygons P\_1, P\_2, \ldots, P\_M."

Here, we regard a point is also contained in a polygon if the point is on the polygon's boundary.

### Constraints

* 3 \leq N \leq 50
* 1 \leq M \leq 2 \times 10^5
* 1 \leq Q \leq 2 \times 10^5
* -10^8 \leq x\_i, y\_i \leq 10^8
* -10^8 \leq u\_i, v\_i \leq 10^8
* -10^8 \leq a\_i, b\_i \leq 10^8
* All values in input are integers.
* (x\_1, y\_1), (x\_2, y\_2), \ldots, (x\_N, y\_N) forms a convex N-gon in the counterclockwise order.
* Each interior angle of the polygon P is less than 180 degrees.

---

### Input

Input is given from Standard Input in the following format:

```
N
x_1 y_1
x_2 y_2
\vdots
x_N y_N
M
u_1 v_1
u_2 v_2
\vdots
u_M v_M
Q
a_1 b_1
a_2 b_2
\vdots
a_Q b_Q
```

### Output

Print Q lines. For i = 1, 2, \ldots, Q, the i-th line should contain `Yes` if point (a\_i, b\_i) is contained in all of the M polygons P\_1, P\_2, \ldots, P\_M; it should contain `No` otherwise.

---

### Sample Input 1

```
5
-2 -3
0 -2
1 0
0 2
-2 1
2
0 1
1 0
6
0 0
1 0
0 1
1 1
-1 -1
-1 -2
```

### Sample Output 1

```
Yes
No
Yes
Yes
Yes
No
```

Polygon P is a pentagon (5-gon) whose vertices are (-2, -3), (0, -2), (1, 0), (0, 2), (-2, 1).

* Polygon P\_1 is a pentagon (5-gon) obtained by shifting P in the positive direction of the x-axis by 0 and in the positive direction of the y-axis by 1, so its vertices are (-2, -2), (0, -1), (1, 1), (0, 3), (-2, 2).
* Polygon P\_2 is a pentagon (5-gon) obtained by shifting P in the positive direction of the x-axis by 1 and in the positive direction of the y-axis by 0, so its vertices are (-1, -3), (1, -2), (2, 0), (1, 2), (-1, 1).

Thus, the following 6 lines should be printed.

* The 1-st line should be `Yes` because (a\_1, b\_1) = (0, 0) is contained in both P\_1 and P\_2.
* The 2-nd line should be `No` because (a\_2, b\_2) = (1, 0) is contained in P\_2 but not in P\_1.
* The 3-rd line should be `Yes` because (a\_3, b\_3) = (0, 1) is contained in both P\_1 and P\_2.
* The 4-th line should be `Yes` because (a\_4, b\_4) = (1, 1) is contained in both P\_1 and P\_2.
* The 5-th line should be `Yes` because (a\_5, b\_5) = (-1, -1) is contained in both P\_1 and P\_2.
* The 6-th line should be `No` because (a\_6, b\_6) = (-1, -2) is contained in P\_2 but not in P\_1.

Note that a point on the boundary of a polygon is also considered to be contained in the polygon.

![](https://img.atcoder.jp/abc251/8216bd194340d2648ce000e9ac9a203e.png)

---

### Sample Input 2

```
10
45 100
-60 98
-95 62
-95 28
-78 -41
-54 -92
-8 -99
87 -94
98 23
87 91
5
-57 -40
-21 -67
25 39
-30 25
39 -20
16
4 5
-34 -8
-63 53
78 84
19 -16
64 9
-13 7
13 53
-20 4
2 -7
3 18
-12 10
-69 -93
2 9
27 64
-92 -100
```

### Sample Output 2

```
Yes
Yes
No
No
Yes
No
Yes
No
Yes
Yes
Yes
Yes
No
Yes
No
No
```
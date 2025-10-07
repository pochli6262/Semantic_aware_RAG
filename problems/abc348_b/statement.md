Score: 200 points

### Problem Statement

On the xy-plane, there are N points with ID numbers from 1 to N. Point i is located at coordinates (X\_i, Y\_i), and no two points have the same coordinates.

From each point, find the farthest point and print its ID number.
If multiple points are the farthest, print the smallest of the ID numbers of those points.

Here, we use the Euclidean distance: for two points (x\_1,y\_1) and (x\_2,y\_2), the distance between them is \sqrt{(x\_1-x\_2)^{2}+(y\_1-y\_2)^{2}}.

### Constraints

* 2 \leq N \leq 100
* -1000 \leq X\_i, Y\_i \leq 1000
* (X\_i, Y\_i) \neq (X\_j, Y\_j) if i \neq j.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
X_1 Y_1
X_2 Y_2
\vdots
X_N Y_N
```

### Output

Print N lines. The i-th line should contain the ID number of the farthest point from point i.

---

### Sample Input 1

```
4
0 0
2 4
5 0
3 4
```

### Sample Output 1

```
3
3
1
1
```

The following figure shows the arrangement of the points. Here, P\_i represents point i.
![](https://img.atcoder.jp/abc348/74796471c6f7ac6134b3b2aa014eea96.png)
The farthest point from point 1 are points 3 and 4, and point 3 has the smaller ID number.

The farthest point from point 2 is point 3.

The farthest point from point 3 are points 1 and 2, and point 1 has the smaller ID number.

The farthest point from point 4 is point 1.

---

### Sample Input 2

```
6
3 2
1 6
4 5
1 3
5 5
9 8
```

### Sample Output 2

```
6
6
6
6
6
4
```
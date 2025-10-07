Score : 100 points

### Problem Statement

There is a rectangle in the xy-plane. Each edge of this rectangle is parallel to the x- or y-axis, and its area is not zero.

Given the coordinates of three of the four vertices of this rectangle, (x\_1, y\_1), (x\_2, y\_2), and (x\_3, y\_3), find the coordinates of the other vertex.

### Constraints

* -100 \leq x\_i, y\_i \leq 100
* There uniquely exists a rectangle with all of (x\_1, y\_1), (x\_2, y\_2), (x\_3, y\_3) as vertices, edges parallel to the x- or y-axis, and a non-zero area.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
x_1 y_1
x_2 y_2
x_3 y_3
```

### Output

Print the sought coordinates (x, y) separated by a space in the following format:

```
x y
```

---

### Sample Input 1

```
-1 -1
-1 2
3 2
```

### Sample Output 1

```
3 -1
```

The other vertex of the rectangle with vertices (-1, -1), (-1, 2), (3, 2) is (3, -1).

---

### Sample Input 2

```
-60 -40
-60 -80
-20 -80
```

### Sample Output 2

```
-20 -40
```
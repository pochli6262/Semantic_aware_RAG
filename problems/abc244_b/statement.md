Score : 200 points

### Problem Statement

Consider an xy-plane. The positive direction of the x-axis is in the direction of east, and the positive direction of the y-axis is in the direction of north.  
Takahashi is initially at point (x, y) = (0, 0) and facing east (in the positive direction of the x-axis).

You are given a string T = t\_1t\_2\ldots t\_N of length N consisting of `S` and `R`.
Takahashi will do the following move for each i = 1, 2, \ldots, N in this order.

* If t\_i = `S`, Takahashi advances in the current direction by distance 1.
* If t\_i = `R`, Takahashi turns 90 degrees clockwise without changing his position. As a result, Takahashi's direction changes as follows.
  + If he is facing east (in the positive direction of the x-axis) before he turns, he will face south (in the negative direction of the y-axis) after he turns.
  + If he is facing south (in the negative direction of the y-axis) before he turns, he will face west (in the negative direction of the x-axis) after he turns.
  + If he is facing west (in the negative direction of the x-axis) before he turns, he will face north (in the positive direction of the y-axis) after he turns.
  + If he is facing north (in the positive direction of the y-axis) before he turns, he will face east (in the positive direction of the x-axis) after he turns.

Print the coordinates Takahashi is at after all the steps above have been done.

### Constraints

* 1 \leq N \leq 10^5
* N is an integer.
* T is a string of length N consisting of `S` and `R`.

---

### Input

Input is given from Standard Input in the following format:

```
N
T
```

### Output

Print the coordinates (x, y) Takahashi is at after all the steps described in the Problem Statement have been completed, in the following format, with a space in between:

```
x y
```

---

### Sample Input 1

```
4
SSRS
```

### Sample Output 1

```
2 -1
```

Takahashi is initially at (0, 0) facing east. Then, he moves as follows.

1. t\_1 = `S`, so he advances in the direction of east by distance 1, arriving at (1, 0).
2. t\_2 = `S`, so he advances in the direction of east by distance 1, arriving at (2, 0).
3. t\_3 = `R`, so he turns 90 degrees clockwise, resulting in facing south.
4. t\_4 = `S`, so he advances in the direction of south by distance 1, arriving at (2, -1).

Thus, Takahashi's final position, (x, y) = (2, -1), should be printed.

---

### Sample Input 2

```
20
SRSRSSRSSSRSRRRRRSRR
```

### Sample Output 2

```
0 1
```
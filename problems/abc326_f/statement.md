Score : 525 points

### Problem Statement

A robot is at the origin of a coordinate plane where the positive x-axis points to the right and the positive y-axis points upwards. Initially, the robot is facing the positive x-direction.

You will perform the following operation for i=1,\ldots,N in this order.

* Rotate the robot 90 degrees clockwise or counterclockwise. Then, the robot moves forward A\_i units in the direction it is facing.

Can the direction of rotation be chosen so that the robot will be at the coordinates (X,Y) after the N operations?

If it is possible, determine which direction, clockwise or counterclockwise, should be chosen for each operation.

### Constraints

* 1 \leq N \leq 80
* 1 \leq A\_i \leq 10^7
* -10^9\leq X,Y \leq 10^9
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N X Y
A_1 \ldots A_N
```

### Output

If the robot cannot be at the coordinates (X,Y) after the N operations, print `No`.  
If the robot can be at the coordinates (X,Y) after the N operations, the first line should contain `Yes`, and the second line should contain a string S of length N that satisfies the following condition.  
Condition: S consists of `L` and `R`, and the following choices can put the robot at the coordinates (X,Y) after the N operations: in the i-th operation, rotate the robot counterclockwise if the i-th character of S is `L`, and rotate it clockwise if it is `R`.

If there are multiple solutions, you may print any of them.

---

### Sample Input 1

```
3 -2 4
3 2 1
```

### Sample Output 1

```
Yes
LLR
```

Initially, the robot is at (0,0) and facing the positive x-direction. The following choices can put the robot at the coordinates (X,Y) after the N operations.

* First operation: Rotate the robot 90 degrees counterclockwise to face the positive y-direction. The robot moves forward A\_1=3 units in the direction it is facing, and moves to (0,3).
* Second operation: Rotate the robot 90 degrees counterclockwise to face the negative x-direction. The robot moves forward A\_2=2 units in the direction it is facing, and moves to (-2,3).
* Third operation: Rotate the robot 90 degrees clockwise to face the positive y-direction. The robot moves forward A\_3=1 unit in the direction it is facing, and moves to (-2,4).

![Diagram](https://img.atcoder.jp/abc326/79baf4537d56c0df5c5d254e6e7f9616.png)

---

### Sample Input 2

```
1 0 0
1
```

### Sample Output 2

```
No
```

---

### Sample Input 3

```
4 0 0
1 1 1 1
```

### Sample Output 3

```
Yes
LRRR
```

Outputs such as `LLLL` and `RRRR` are also accepted.

---

### Sample Input 4

```
14 2543269 -1705099
3 14 159 2653 58979 323846 2643383 2795028 841971 69399 37510 58 20 9
```

### Sample Output 4

```
Yes
LLLLLLLLLRLRRR
```
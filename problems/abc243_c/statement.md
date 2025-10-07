Score : 300 points

### Problem Statement

There are N people in an xy-plane. Person i is at (X\_i, Y\_i). The positions of all people are different.

We have a string S of length N consisting of `L` and `R`.  
If S\_i = `R`, Person i is facing right; if S\_i = `L`, Person i is facing left. All people simultaneously start walking in the direction they are facing. Here, right and left correspond to the positive and negative x-direction, respectively.

For example, the figure below shows the movement of people when (X\_1, Y\_1) = (2, 3), (X\_2, Y\_2) = (1, 1), (X\_3, Y\_3) =(4, 1), S = `RRL`.

![image](https://img.atcoder.jp/ghi/f33104f8bc05a920f2b74ead8ad1e3d2.png)

We say that there is a collision when two people walking in opposite directions come to the same position. Will there be a collision if all people continue walking indefinitely?

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 0 \leq X\_i \leq 10^9
* 0 \leq Y\_i \leq 10^9
* (X\_i, Y\_i) \neq (X\_j, Y\_j) if i \neq j.
* All X\_i and Y\_i are integers.
* S is a string of length N consisting of `L` and `R`.

---

### Input

Input is given from Standard Input in the following format:

```
N
X_1 Y_1
X_2 Y_2
\vdots
X_N Y_N
S
```

### Output

If there will be a collision, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3
2 3
1 1
4 1
RRL
```

### Sample Output 1

```
Yes
```

This input corresponds to the example in the Problem Statement.  
If all people continue walking, Person 2 and Person 3 will collide. Thus, `Yes` should be printed.

---

### Sample Input 2

```
2
1 1
2 1
RR
```

### Sample Output 2

```
No
```

Since Person 1 and Person 2 walk in the same direction, they never collide.

---

### Sample Input 3

```
10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR
```

### Sample Output 3

```
Yes
```
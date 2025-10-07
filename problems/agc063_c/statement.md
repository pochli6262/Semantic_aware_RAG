Score : 800 points

### Problem Statement

You are given sequences of non-negative integers: A = (A\_1, \ldots, A\_N) and B=(B\_1, \ldots, B\_N).

Determine whether one can make A equal B by performing the following operation between 0 and N times, inclusive.

* Operation: Choose integers x,y such that 0\leq x < y\leq 10^{18}. For every i, replace A\_i with (A\_i+x)\bmod y.

If one can make A equal B, print one way to do so.

### Constraints

* 1\leq N\leq 1000
* 0\leq A\_i\leq 10^9
* 0\leq B\_i\leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 \ldots A_N
B_1 \ldots B_N
```

### Output

If one cannot make A equal B by performing the operation between 0 and N times, inclusive, print `No`.

```
No
```

If one can do so, print one way in the following format:

```
Yes
K
x_1 y_1
\vdots
x_K y_K
```

Here, K is the number of operations, and x\_i, y\_i are integers x, y chosen in the i-th operation. These must satisfy the following:

* 0\leq K\leq N
* 0\leq x\_i < y\_i \leq 10^{18}

If there are multiple ways to achieve the objective, you may print any of them.

---

### Sample Input 1

```
4
7 2 4 5
3 3 5 0
```

### Sample Output 1

```
Yes
2
3 5
3 6
```

One can make A equal B as follows.

* Initially, A = (7,2,4,5).
* The operation with (x,y) = (3,5) makes A = (0,0,2,3).
* The operation with (x,y) = (3,6) makes A = (3,3,5,0).

---

### Sample Input 2

```
1
5
3
```

### Sample Output 2

```
Yes
1
2 4
```

---

### Sample Input 3

```
2
3 1
3 1
```

### Sample Output 3

```
Yes
0
```

---

### Sample Input 4

```
2
0 0
1 2
```

### Sample Output 4

```
No
```
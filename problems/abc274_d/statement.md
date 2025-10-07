Score : 400 points

### Problem Statement

You are given a sequence A = (A\_1, A\_2, \dots, A\_N) of length N consisting of positive integers, and integers x and y.  
Determine whether it is possible to place N+1 points p\_1, p\_2, \dots, p\_N, p\_{N+1} in the xy-coordinate plane to satisfy all of the following conditions. (It is allowed to place two or more points at the same coordinates.)

* p\_1 = (0, 0).
* p\_2 = (A\_1, 0).
* p\_{N+1} = (x, y).
* The distance between the points p\_i and p\_{i+1} is A\_i. (1 \leq i \leq N)
* The segments p\_i p\_{i+1} and p\_{i+1} p\_{i+2} form a 90 degree angle. (1 \leq i \leq N - 1)

### Constraints

* 2 \leq N \leq 10^3
* 1 \leq A\_i \leq 10
* |x|, |y| \leq 10^4
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N x y
A_1 A_2 \dots A_N
```

### Output

If it is possible to place p\_1, p\_2, \dots, p\_N, p\_{N+1} to satisfy all of the conditions in the Problem Statement, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3 -1 1
2 1 3
```

### Sample Output 1

```
Yes
```

The figure below shows a placement where p\_1 = (0, 0), p\_2 = (2, 0), p\_3 = (2, 1), and p\_4 = (-1, 1). All conditions in the Problem Statement are satisfied.

![](https://img.atcoder.jp/ghi/9e66a2e8cd081f011d3baba22dbe64fa.jpg)

---

### Sample Input 2

```
5 2 0
2 2 2 2 2
```

### Sample Output 2

```
Yes
```

Letting p\_1 = (0, 0), p\_2 = (2, 0), p\_3 = (2, 2), p\_4 = (0, 2), p\_5 = (0, 0), and p\_6 = (2, 0) satisfies all the conditions. Note that multiple points may be placed at the same coordinates.

---

### Sample Input 3

```
4 5 5
1 2 3 4
```

### Sample Output 3

```
No
```

---

### Sample Input 4

```
3 2 7
2 7 4
```

### Sample Output 4

```
No
```

---

### Sample Input 5

```
10 8 -7
6 10 4 1 5 9 8 6 5 1
```

### Sample Output 5

```
Yes
```
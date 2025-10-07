Score : 500 points

### Problem Statement

You are given non-zero integers x\_1, \ldots, x\_N. Find the minimum and maximum values of \dfrac{x\_i+x\_j+x\_k}{x\_ix\_jx\_k} for integers i, j, k such that 1\leq i < j < k\leq N.

### Constraints

* 3\leq N\leq 2\times 10^5
* -10^6\leq x\_i \leq 10^6
* x\_i\neq 0

---

### Input

The input is given from Standard Input in the following format:

```
N
x_1 \ldots x_N
```

### Output

Print the minimum value of \dfrac{x\_i+x\_j+x\_k}{x\_ix\_jx\_k} in the first line and the maximum value in the second line.

Your output will be considered correct when the absolute or relative error is at most 10^{-12}.

---

### Sample Input 1

```
4
-2 -4 4 5
```

### Sample Output 1

```
-0.175000000000000
-0.025000000000000
```

\dfrac{x\_i+x\_j+x\_k}{x\_ix\_jx\_k} can take the following four values.

* (i,j,k) = (1,2,3): \dfrac{(-2) + (-4) + 4}{(-2)\cdot (-4)\cdot 4} = -\dfrac{1}{16}.
* (i,j,k) = (1,2,4): \dfrac{(-2) + (-4) + 5}{(-2)\cdot (-4)\cdot 5} = -\dfrac{1}{40}．
* (i,j,k) = (1,3,4): \dfrac{(-2) + 4 + 5}{(-2)\cdot 4\cdot 5} = -\dfrac{7}{40}．
* (i,j,k) = (2,3,4): \dfrac{(-4) + 4 + 5}{(-4)\cdot 4\cdot 5} = -\dfrac{1}{16}.

Among them, the minimum is -\dfrac{7}{40}, and the maximum is -\dfrac{1}{40}.

---

### Sample Input 2

```
4
1 1 1 1
```

### Sample Output 2

```
3.000000000000000
3.000000000000000
```

---

### Sample Input 3

```
5
1 2 3 4 5
```

### Sample Output 3

```
0.200000000000000
1.000000000000000
```
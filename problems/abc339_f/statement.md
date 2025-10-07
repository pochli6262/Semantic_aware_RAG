Score: 550 points

### Problem Statement

You are given N integers A\_1, A\_2, \dots, A\_N.  
Find the number of triples of integers (i, j, k) that satisfy the following conditions:

* 1 \le i, j, k \le N
* A\_i \times A\_j = A\_k

### Constraints

* 1 \le N \le 1000
* \color{red}{1 \le A\_i < 10^{1000}}

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1
A_2
\vdots
A_N
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
5
2
3
6
12
24
```

### Sample Output 1

```
6
```

The following six triples (i, j, k) satisfy the conditions in the problem statement:

* (1, 2, 3)
* (1, 3, 4)
* (1, 4, 5)
* (2, 1, 3)
* (3, 1, 4)
* (4, 1, 5)

---

### Sample Input 2

```
11
1
2
3
4
5
6
123456789123456789
123456789123456789
987654321987654321
987654321987654321
121932631356500531347203169112635269
```

### Sample Output 2

```
40
```

Note that the values of each integer A\_i can be huge.

---

### Sample Input 3

```
9
4
4
4
2
2
2
1
1
1
```

### Sample Output 3

```
162
```

Note that there may be duplicates among the values of A\_i.
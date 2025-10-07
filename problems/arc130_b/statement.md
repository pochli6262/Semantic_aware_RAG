Score : 400 points

### Problem Statement

We have an H\times W grid. Initially, the squares are unpainted.

You will paint these squares. There are C colors available, numbered 1, 2, \ldots, C.

The painting process will be given as Q queries. The i-th query contains integers t\_i, n\_i, c\_i, which represents the following action.

* If t\_i = 1: paint all squares in the n\_i-th **row** with Color c\_i.
* If t\_i = 2: paint all squares in the n\_i-th **column** with Color c\_i.

Painting a square with Color c makes the color of that square Color c, regardless of its previous state.

Find the number of squares painted in each of Color 1, 2, \ldots, C after the whole process.

### Constraints

* 2\leq H\leq 10^9
* 2\leq W\leq 10^9
* 1\leq C\leq 3\times 10^5
* 1\leq Q\leq 3\times 10^5
* t\_i\in \{1,2\}
* 1\leq n\_i\leq H if t\_i = 1
* 1\leq n\_i\leq W if t\_i = 2
* 1\leq c\_i\leq C

---

### Input

Input is given from Standard Input in the following format:

```
H W C Q
t_1 n_1 c_1
\vdots
t_Q n_Q c_Q
```

### Output

Print a line containing the numbers of squares painted in Color 1, 2, \ldots, C, with spaces in between.

---

### Sample Input 1

```
4 5 6 5
1 1 6
1 3 3
2 2 4
2 4 2
1 1 2
```

### Sample Output 1

```
0 8 3 3 0 0
```

The process changes the colors of the squares as follows. Here, `.` denotes an unpainted square.

```
.....   66666   66666   64666   64626   22222
.....   .....   .....   .4...   .4.2.   .4.2.
.....   .....   33333   34333   34323   34323
.....   .....   .....   .4...   .4.2.   .4.2.
```

---

### Sample Input 2

```
1000000000 1000000000 3 5
1 1 2
1 2 2
1 3 2
1 4 2
1 5 2
```

### Sample Output 2

```
0 5000000000 0
```
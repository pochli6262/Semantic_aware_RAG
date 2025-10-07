Score : 500 points

### Problem Statement

There are N items.  
Each of these is one of a pull-tab can, a regular can, or a can opener.  
The i-th item is described by an integer pair (T\_i, X\_i) as follows:

* If T\_i = 0, the i-th item is a pull-tab can; if you obtain it, you get a happiness of X\_i.
* If T\_i = 1, the i-th item is a regular can; if you obtain it and use a can opener against it, you get a happiness of X\_i.
* If T\_i = 2, the i-th item is a can opener; it can be used against at most X\_i cans.

Find the maximum total happiness that you get by obtaining M items out of N.

### Constraints

* 1 \leq M \leq N \leq 2 \times 10^5
* T\_i is 0, 1, or 2.
* 1 \leq X\_i \leq 10^9
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
T_1 X_1
T_2 X_2
\vdots
T_N X_N
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
8 4
0 6
0 6
1 3
1 5
1 15
2 1
2 10
2 100
```

### Sample Output 1

```
27
```

If you obtain the 1-st, 2-nd, 5-th, and 7-th items, and use the 7-th item (a can opener) against the 5-th item, you will get a happiness of 6 + 6 + 15 = 27.  
There are no ways to obtain items to get a happiness of 28 or greater, but you can still get a happiness of 27 by obtaining the 6-th or 8-th items instead of the 7-th in the combination above.

---

### Sample Input 2

```
5 5
1 5
1 5
1 5
1 5
1 5
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
12 6
2 2
0 1
0 9
1 3
1 5
1 3
0 4
2 1
1 8
2 1
0 1
0 4
```

### Sample Output 3

```
30
```
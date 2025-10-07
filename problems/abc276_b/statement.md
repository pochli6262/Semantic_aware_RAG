Score : 200 points

### Problem Statement

There are N cities numbered 1, \dots, N, and M roads connecting cities.  
The i-th road (1 \leq i \leq M) connects city A\_i and city B\_i.

Print N lines as follows.

* Let d\_i be the number of cities directly connected to city i \, (1 \leq i \leq N), and those cities be city a\_{i, 1}, \dots, city a\_{i, d\_i}, in **ascending order**.
* The i-th line (1 \leq i \leq N) should contain d\_i + 1 integers d\_i, a\_{i, 1}, \dots, a\_{i, d\_i} in this order, separated by spaces.

### Constraints

* 2 \leq N \leq 10^5
* 1 \leq M \leq 10^5
* 1 \leq A\_i \lt B\_i \leq N \, (1 \leq i \leq M)
* (A\_i, B\_i) \neq (A\_j, B\_j) if (i \neq j).
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 B_1
\vdots
A_M B_M
```

### Output

Print N lines as specified in the Problem Statement.

---

### Sample Input 1

```
6 6
3 6
1 3
5 6
2 5
1 2
1 6
```

### Sample Output 1

```
3 2 3 6
2 1 5
2 1 6
0
2 2 6
3 1 3 5
```

The cities directly connected to city 1 are city 2, city 3, and city 6. Thus, we have d\_1 = 3, a\_{1, 1} = 2, a\_{1, 2} = 3, a\_{1, 3} = 6, so you should print 3, 2, 3, 6 in the first line in this order, separated by spaces.

Note that a\_{i, 1}, \dots, a\_{i, d\_i} must be in ascending order. For instance, it is unacceptable to print 3, 3, 2, 6 in the first line in this order.

---

### Sample Input 2

```
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
```

### Sample Output 2

```
4 2 3 4 5
4 1 3 4 5
4 1 2 4 5
4 1 2 3 5
4 1 2 3 4
```
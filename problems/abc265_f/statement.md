Score : 500 points

### Problem Statement

In an N-dimensional space, the Manhattan distance d(x,y) between two points x=(x\_1, x\_2, \dots, x\_N) and y = (y\_1, y\_2, \dots, y\_N) is defined by:

\displaystyle d(x,y)=\sum\_{i=1}^n \vert x\_i - y\_i \vert.

A point x=(x\_1, x\_2, \dots, x\_N) is said to be a lattice point if the components x\_1, x\_2, \dots, x\_N are all integers.

You are given lattice points p=(p\_1, p\_2, \dots, p\_N) and q = (q\_1, q\_2, \dots, q\_N) in an N-dimensional space.  
How many lattice points r satisfy d(p,r) \leq D and d(q,r) \leq D? Find the count modulo 998244353.

### Constraints

* 1 \leq N \leq 100
* 0 \leq D \leq 1000
* -1000 \leq p\_i, q\_i \leq 1000
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N D 
p_1 p_2 \dots p_N
q_1 q_2 \dots q_N
```

### Output

Print the answer.

---

### Sample Input 1

```
1 5
0
3
```

### Sample Output 1

```
8
```

When N=1, we consider points in a one-dimensional space, that is, on a number line.  
8 lattice points satisfy the conditions: -2,-1,0,1,2,3,4,5.

---

### Sample Input 2

```
3 10
2 6 5
2 1 2
```

### Sample Output 2

```
632
```

---

### Sample Input 3

```
10 100
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8
```

### Sample Output 3

```
145428186
```
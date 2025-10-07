Score: 600 points

### Problem Statement

There is a tree with N vertices numbered 1 to N. The i-th edge connects vertices u\_i and v\_i.  
Additionally, there are N pieces numbered 1 to N. Initially, piece i is placed on vertex i.  
You can perform the following operation any number of times, possibly zero:

* Choose one edge. Let vertices u and v be the endpoints of the edge, and swap the pieces on vertices u and v. Then, delete the chosen edge.

Let a\_i be the piece on vertex i. How many different possible sequences (a\_1, a\_2, \dots, a\_N) exist when you finish performing the operation? Find the count modulo 998244353.

### Constraints

* 2 \leq N \leq 3000
* 1 \leq u\_i \lt v\_i \leq N
* The graph given in the input is a tree.

---

### Input

The input is given from Standard Input in the following format:

```
N
u_1 v_1
u_2 v_2
\vdots
u_{N-1} v_{N-1}
```

### Output

Print the number, modulo 998244353, of possible sequences (a\_1, a\_2, \dots, a\_N).

---

### Sample Input 1

```
3
1 2
2 3
```

### Sample Output 1

```
5
```

For example, the sequence (a\_1, a\_2, a\_3) = (2, 1, 3) can be obtained by the following steps:

* Choose the first edge, swap the pieces on vertices 1 and 2, and delete the edge. This results in (a\_1, a\_2, a\_3) = (2, 1, 3).
* Finish operating.

Also, the sequence (a\_1, a\_2, a\_3) = (3, 1, 2) can be obtained by the following steps:

* Choose the second edge, swap the pieces on vertices 2 and 3, and delete the edge. This results in (a\_1, a\_2, a\_3) = (1, 3, 2).
* Choose the first edge, swap the pieces on vertices 1 and 2, and delete the edge. This results in (a\_1, a\_2, a\_3) = (3, 1, 2).
* Finish operating.

The operation can yield the following five sequences:

* (1, 2, 3)
* (1, 3, 2)
* (2, 1, 3)
* (2, 3, 1)
* (3, 1, 2)

---

### Sample Input 2

```
5
2 5
3 4
1 3
1 5
```

### Sample Output 2

```
34
```

---

### Sample Input 3

```
8
4 5
2 5
3 6
1 3
1 8
2 7
2 8
```

### Sample Output 3

```
799
```
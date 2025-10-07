Score : 800 points

### Problem Statement

We have a grid with N \times M squares. You will fill every square with an integer between 1 and 25 (inclusive). Let a\_{i,j} be the integer to be written in the square at the i-th row from the top and j-th column from the left.

Find a way to fill the squares to satisfy the condition below. It can be proved that, under the Constraints of this problem, such a way always exists.

* For any integers 1\leq x\_1 < x\_2\leq N,1\leq y\_1 < y\_2 \leq M, it must not be the case that a\_{x\_1,y\_1},a\_{x\_1,y\_2},a\_{x\_2,y\_1},a\_{x\_2,y\_2} are all equal.

### Constraints

* 2 \leq N , M \leq 500
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M 
```

### Output

Print one way to fill the squares to satisfy the condition, in the format below:

```
a_{1,1} a_{1,2} \ldots a_{1,M}
a_{2,1} a_{2,2} \ldots a_{2,M}
\vdots
a_{N,1} a_{N,2} \ldots a_{N,M}
```

If there are multiple solutions, printing any of them will be accepted.

---

### Sample Input 1

```
2 3
```

### Sample Output 1

```
1 1 1
1 2 3
```

(x\_1,x\_2,y\_1,y\_2) can be one of (1,2,1,2),(1,2,2,3),(1,2,1,3).

For any of them, the numbers written in the squares are not all equal, so this output satisfies the condition.
Score : 200 points

### Problem Statement

We have a grid with H horizontal rows and W vertical columns, where each square contains an integer.
The integer written on the square at the i-th row from the top and j-th column from the left is A\_{i, j}.

Determine whether the grid satisfies the condition below.

> A\_{i\_1, j\_1} + A\_{i\_2, j\_2} \leq A\_{i\_2, j\_1} + A\_{i\_1, j\_2} holds for every quadruple of integers (i\_1, i\_2, j\_1, j\_2) such that 1 \leq i\_1 < i\_2 \leq H and 1 \leq j\_1 < j\_2 \leq W.

### Constraints

* 2 \leq H, W \leq 50
* 1 \leq A\_{i, j} \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
H W
A_{1, 1} A_{1, 2} \cdots A_{1, W}
A_{2, 1} A_{2, 2} \cdots A_{2, W}
\vdots
A_{H, 1} A_{H, 2} \cdots A_{H, W}
```

### Output

If the grid satisfies the condition in the Problem Statement, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3 3
2 1 4
3 1 3
6 4 1
```

### Sample Output 1

```
Yes
```

There are nine quadruples of integers (i\_1, i\_2, j\_1, j\_2) such that 1 \leq i\_1 < i\_2 \leq H and 1 \leq j\_1 < j\_2 \leq W. For all of them, A\_{i\_1, j\_1} + A\_{i\_2, j\_2} \leq A\_{i\_2, j\_1} + A\_{i\_1, j\_2} holds. Some examples follow.

* For (i\_1, i\_2, j\_1, j\_2) = (1, 2, 1, 2), we have A\_{i\_1, j\_1} + A\_{i\_2, j\_2} = 2 + 1 \leq 3 + 1 = A\_{i\_2, j\_1} + A\_{i\_1, j\_2}.
* For (i\_1, i\_2, j\_1, j\_2) = (1, 2, 1, 3), we have A\_{i\_1, j\_1} + A\_{i\_2, j\_2} = 2 + 3 \leq 3 + 4 = A\_{i\_2, j\_1} + A\_{i\_1, j\_2}.
* For (i\_1, i\_2, j\_1, j\_2) = (1, 2, 2, 3), we have A\_{i\_1, j\_1} + A\_{i\_2, j\_2} = 1 + 3 \leq 1 + 4 = A\_{i\_2, j\_1} + A\_{i\_1, j\_2}.
* For (i\_1, i\_2, j\_1, j\_2) = (1, 3, 1, 2), we have A\_{i\_1, j\_1} + A\_{i\_2, j\_2} = 2 + 4 \leq 6 + 1 = A\_{i\_2, j\_1} + A\_{i\_1, j\_2}.
* For (i\_1, i\_2, j\_1, j\_2) = (1, 3, 1, 3), we have A\_{i\_1, j\_1} + A\_{i\_2, j\_2} = 2 + 1 \leq 6 + 4 = A\_{i\_2, j\_1} + A\_{i\_1, j\_2}.

We can also see that the property holds for the other quadruples: (i\_1, i\_2, j\_1, j\_2) = (1, 3, 2, 3), (2, 3, 1, 2), (2, 3, 1, 3), (2, 3, 2, 3).  
Thus, we should print `Yes`.

---

### Sample Input 2

```
2 4
4 3 2 1
5 6 7 8
```

### Sample Output 2

```
No
```

We should print `No` because the condition is not satisfied.  
This is because, for example, we have A\_{i\_1, j\_1} + A\_{i\_2, j\_2} = 4 + 8 > 5 + 1 = A\_{i\_2, j\_1} + A\_{i\_1, j\_2} for (i\_1, i\_2, j\_1, j\_2) = (1, 2, 1, 4).
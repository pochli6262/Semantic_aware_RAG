Score : 200 points

### Problem Statement

You are given N-by-N matrices A and B where each element is 0 or 1.  
Let A\_{i,j} and B\_{i,j} denote the element at the i-th row and j-th column of A and B, respectively.  
Determine whether it is possible to rotate A so that B\_{i,j} = 1 for every pair of integers (i, j) such that A\_{i,j} = 1.  
Here, to rotate A is to perform the following operation zero or more times:

* for every pair of integers (i, j) such that 1 \leq i, j \leq N, simultaneously replace A\_{i,j} with A\_{N + 1 - j,i}.

### Constraints

* 1 \leq N \leq 100
* Each element of A and B is 0 or 1.
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_{1,1} A_{1,2} \ldots A_{1,N}
\vdots
A_{N,1} A_{N,2} \ldots A_{N,N}
B_{1,1} B_{1,2} \ldots B_{1,N}
\vdots
B_{N,1} B_{N,2} \ldots B_{N,N}
```

### Output

If it is possible to rotate A so that B\_{i,j} = 1 for every pair of integers (i, j) such that A\_{i,j} = 1, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3
0 1 1
1 0 0
0 1 0
1 1 0
0 0 1
1 1 1
```

### Sample Output 1

```
Yes
```

Initially, A is :

```
0 1 1
1 0 0
0 1 0
```

After performing the operation once, A is :

```
0 1 0
1 0 1 
0 0 1
```

After performing the operation once again, A is :

```
0 1 0
0 0 1
1 1 0
```

Here, B\_{i,j} = 1 for every pair of integers (i, j) such that A\_{i,j} = 1, so you should print `Yes`.

---

### Sample Input 2

```
2
0 0
0 0
1 1
1 1
```

### Sample Output 2

```
Yes
```

---

### Sample Input 3

```
5
0 0 1 1 0
1 0 0 1 0
0 0 1 0 1
0 1 0 1 0
0 1 0 0 1
1 1 0 0 1
0 1 1 1 0
0 0 1 1 1
1 0 1 0 1
1 1 0 1 0
```

### Sample Output 3

```
No
```
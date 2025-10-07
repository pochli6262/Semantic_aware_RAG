Score: 150 points

### Problem Statement

You are given two grids, each with N rows and N columns, referred to as grid A and grid B.  
Each cell in the grids contains a lowercase English letter.  
The character at the i-th row and j-th column of grid A is A\_{i, j}.  
The character at the i-th row and j-th column of grid B is B\_{i, j}.

The two grids differ in exactly one cell. That is, there exists exactly one pair (i, j) of positive integers not greater than N such that A\_{i, j} \neq B\_{i, j}. Find this (i, j).

### Constraints

* 1 \leq N \leq 100
* A\_{i, j} and B\_{i, j} are all lowercase English letters.
* There exists exactly one pair (i, j) such that A\_{i, j} \neq B\_{i, j}.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_{1,1}A_{1,2}\dots A_{1,N}
A_{2,1}A_{2,2}\dots A_{2,N}
\vdots
A_{N,1}A_{N,2}\dots A_{N,N}
B_{1,1}B_{1,2}\dots B_{1,N}
B_{2,1}B_{2,2}\dots B_{2,N}
\vdots
B_{N,1}B_{N,2}\dots B_{N,N}
```

### Output

Let (i, j) be the pair of positive integers not greater than N such that A\_{i, j} \neq B\_{i, j}. Print (i, j) in the following format:

```
i j
```

---

### Sample Input 1

```
3
abc
def
ghi
abc
bef
ghi
```

### Sample Output 1

```
2 1
```

From A\_{2, 1} = `d` and B\_{2, 1} = `b`, we have A\_{2, 1} \neq B\_{2, 1}, so (i, j) = (2, 1) satisfies the condition in the problem statement.

---

### Sample Input 2

```
1
f
q
```

### Sample Output 2

```
1 1
```

---

### Sample Input 3

```
10
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehfk
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj
eixfumagit
vtophbepfe
pxbfgsqcug
ugpugtsxzq
bvfhxyehok
uqyfwtmglr
jaitenfqiq
acwvufpfvv
jhaddglpva
aacxsyqvoj
```

### Sample Output 3

```
5 9
```
Score : 600 points

### Problem Statement

Determine whether there is an N-by-N matrix X that satisfies the following conditions, and present one such matrix if it exists. (Let x\_{i,j} denote the element of X at the i-th row from the top and j-th column from the left.)

* x\_{i,j} \in \{ 0,1,2 \} for every i and j (1 \leq i,j \leq N).
* The following holds for each i=1,2,\ldots,Q.
  + Let P = \prod\_{a\_i \leq j \leq b\_i} \prod\_{c\_i \leq k \leq d\_i} x\_{j,k}. Then, P is congruent to e\_i modulo 3.

### Constraints

* 1 \leq N,Q \leq 2000
* 1 \leq a\_i \leq b\_i \leq N
* 1 \leq c\_i \leq d\_i \leq N
* e\_i \in \{0,1,2 \}
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N Q
a_1 b_1 c_1 d_1 e_1
\vdots
a_Q b_Q c_Q d_Q e_Q
```

### Output

If no matrix X satisfies the conditions, print `No`.

If there is a matrix X that satisfies them, print `Yes` in the first line and one such instance of X in the following format in the second and subsequent lines.

```
x_{1,1} x_{1,2} \ldots x_{1,N}
x_{2,1} x_{2,2} \ldots x_{2,N}
\vdots
x_{N,1} x_{N,2} \ldots x_{N,N}
```

If multiple matrices satisfy the conditions, any of them will be accepted.

---

### Sample Input 1

```
2 3
1 1 1 2 0
1 2 2 2 1
2 2 1 2 2
```

### Sample Output 1

```
Yes
0 2
1 2
```

For example, for i=2, we have P = \prod\_{a\_2 \leq j \leq b\_2} \prod\_{c\_2 \leq k \leq d\_2} x\_{j,k}= \prod\_{1 \leq j \leq 2} \prod\_{2 \leq k \leq 2} x\_{j,k}=x\_{1,2} \times x\_{2,2}.  
In this sample output, we have x\_{1,2}=2 and x\_{2,2}=2, so P=2 \times 2 = 4, which is congruent to e\_2=1 modulo 3.  
It can be similarly verified that the condition is also satisfied for i=1 and i=3.

---

### Sample Input 2

```
4 4
1 4 1 4 0
1 4 1 4 1
1 4 1 4 2
1 4 1 4 0
```

### Sample Output 2

```
No
```
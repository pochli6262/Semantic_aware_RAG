Score : 400 points

### Problem Statement

We have a polynomial of degree N, A(x)=A\_Nx^N+A\_{N-1}x^{N-1}+\cdots +A\_1x+A\_0,  
and another of degree M, B(x)=B\_Mx^M+B\_{M-1}x^{M-1}+\cdots +B\_1x+B\_0.  
Here, each coefficient of A(x) and B(x) is an integer whose absolute value is at most 100, and the leading coefficients are not 0.

Also, let the product of them be C(x)=A(x)B(x)=C\_{N+M}x^{N+M}+C\_{N+M-1}x^{N+M-1}+\cdots +C\_1x+C\_0.

Given A\_0,A\_1,\ldots, A\_N and C\_0,C\_1,\ldots, C\_{N+M}, find B\_0,B\_1,\ldots, B\_M.  
Here, the given inputs guarantee that there is a unique sequence B\_0, B\_1, \ldots, B\_M that satisfies the given conditions.

### Constraints

* 1 \leq N < 100
* 1 \leq M < 100
* |A\_i| \leq 100
* |C\_i| \leq 10^6
* A\_N \neq 0
* C\_{N+M} \neq 0
* There is a unique sequence B\_0, B\_1, \ldots, B\_M that satisfies the conditions given in the statement.

---

### Input

Input is given from Standard Input in the following format:

```
N M
A_0 A_1 \ldots A_{N-1} A_N
C_0 C_1 \ldots C_{N+M-1} C_{N+M}
```

### Output

Print the M+1 integers B\_0,B\_1,\ldots, B\_M in one line, with spaces in between.

---

### Sample Input 1

```
1 2
2 1
12 14 8 2
```

### Sample Output 1

```
6 4 2
```

For A(x)=x+2 and B(x)=2x^2+4x+6, we have C(x)=A(x)B(x)=(x+2)(2x^2+4x+6)=2x^3+8x^2+14x+12, so B(x)=2x^2+4x+6 satisfies the given conditions. Thus, B\_0=6, B\_1=4, B\_2=2 should be printed in this order, with spaces in between.

---

### Sample Input 2

```
1 1
100 1
10000 0 -1
```

### Sample Output 2

```
100 -1
```

We have A(x)=x+100, C(x)=-x^2+10000, for which B(x)=-x+100 satisfies the given conditions.
Thus, 100, -1 should be printed in this order, with spaces in between.
Score : 500 points

### Problem Statement

We have a sequence of length N consisting of integers between 0 and M, inclusive: A=(A\_1,A\_2,\dots,A\_N).

Snuke will perform the following operations 1 and 2 in order.

1. For each i such that A\_i=0, independently choose a uniform random integer between 1 and M, inclusive, and replace A\_i with that integer.
2. Sort A in ascending order.

Print the expected value of A\_K after the two operations, modulo 998244353.

How to print a number modulo 998244353?
It can be proved that the sought expected value is always rational.
Additionally, under the Constraints of this problem, when that value is represented as \frac{P}{Q} using two coprime integers P and Q, it can be proved that there is a unique integer R such that R \times Q \equiv P\pmod{998244353} and 0 \leq R \lt 998244353. Print this R.

### Constraints

* 1\leq K \leq N \leq 2000
* 1\leq M \leq 2000
* 0\leq A\_i \leq M
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M K
A_1 A_2 \dots A_N
```

### Output

Print the expected value of A\_K after the two operations, modulo 998244353.

---

### Sample Input 1

```
3 5 2
2 0 4
```

### Sample Output 1

```
3
```

In the operation 1, Snuke will replace A\_2 with an integer between 1 and 5. Let x be this integer.

* If x=1 or 2, we will have A\_2=2 after the two operations.
* If x=3, we will have A\_2=3 after the two operations.
* If x=4 or 5, we will have A\_2=4 after the two operations.

Thus, the expected value of A\_2 is \frac{2+2+3+4+4}{5}=3.

---

### Sample Input 2

```
2 3 1
0 0
```

### Sample Output 2

```
221832080
```

The expected value is \frac{14}{9}.

---

### Sample Input 3

```
10 20 7
6 5 0 2 0 0 0 15 0 0
```

### Sample Output 3

```
617586310
```
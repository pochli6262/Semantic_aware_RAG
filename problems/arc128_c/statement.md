Score : 600 points

### Problem Statement

Given are integers N, M, S, and a sequence of N integers A=(A\_1,A\_2,\cdots,A\_N).

Consider making a sequence of N non-negative **real** numbers x=(x\_1,x\_2,\cdots,x\_N) satisfying all of the following conditions:

* 0 \leq x\_1 \leq x\_2 \leq \cdots \leq x\_N \leq M,
* \sum\_{1 \leq i \leq N} x\_i=S.

Now, let us define the score of x as \sum\_{1 \leq i \leq N} A\_i \times x\_i.
Find the maximum possible score of x.

### Constraints

* 1 \leq N \leq 5000
* 1 \leq M \leq 10^6
* 1 \leq S \leq \min(N \times M,10^6)
* 1 \leq A\_i \leq 10^6
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M S
A_1 A_2 \cdots A_N
```

### Constraints

Print the answer.
Your output will be considered correct if its absolute or relative error is at most 10^{-6}.

---

### Sample Input 1

```
3 2 3
1 2 3
```

### Sample Output 1

```
8.00000000000000000000
```

The optimal choice is x=(0,1,2).

---

### Sample Input 2

```
3 3 2
5 1 1
```

### Sample Output 2

```
4.66666666666666666667
```

The optimal choice is x=(2/3,2/3,2/3).

---

### Sample Input 3

```
10 234567 1000000
353239 53676 45485 617014 886590 423581 172670 928532 312338 981241
```

### Sample Output 3

```
676780145098.25000000000000000000
```
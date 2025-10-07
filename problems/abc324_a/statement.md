Score : 100 points

### Problem Statement

You are given N integers A \_ 1,A \_ 2,\ldots,A \_ N.

If their values are all equal, print `Yes`; otherwise, print `No`.

### Constraints

* 2\leq N\leq100
* 1\leq A \_ i\leq100\ (1\leq i\leq N)
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A _ 1 A _ 2 \ldots A _ N
```

### Output

Print a single line containing `Yes` if the values of the given A \_ 1,A \_ 2,\ldots,A \_ N are all equal, and `No` otherwise.

---

### Sample Input 1

```
3
3 2 4
```

### Sample Output 1

```
No
```

We have A \_ 1\neq A \_ 2, so you should print `No`.

---

### Sample Input 2

```
4
3 3 3 3
```

### Sample Output 2

```
Yes
```

We have A \_ 1=A \_ 2=A \_ 3=A \_ 4, so you should print `Yes`.

---

### Sample Input 3

```
10
73 8 55 26 97 48 37 47 35 55
```

### Sample Output 3

```
No
```
Score : 350 points

### Problem Statement

For a positive integer N, let V\_N be the integer formed by concatenating N exactly N times.  
More precisely, consider N as a string, concatenate N copies of it, and treat the result as an integer to get V\_N.  
For example, V\_3=333 and V\_{10}=10101010101010101010.

Find the remainder when V\_N is divided by 998244353.

### Constraints

* 1 \leq N \leq 10^{18}
* N is an integer.

---

### Input

The input is given from Standard Input in the following format:

```
N
```

### Output

Print the remainder when V\_N is divided by 998244353.

---

### Sample Input 1

```
5
```

### Sample Output 1

```
55555
```

The remainder when V\_5=55555 is divided by 998244353 is 55555.

---

### Sample Input 2

```
9
```

### Sample Output 2

```
1755646
```

The remainder when V\_9=999999999 is divided by 998244353 is 1755646.

---

### Sample Input 3

```
10000000000
```

### Sample Output 3

```
468086693
```

Note that the input may not fit into a 32-bit integer type.
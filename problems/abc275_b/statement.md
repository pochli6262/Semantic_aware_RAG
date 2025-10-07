Score : 200 points

### Problem Statement

There are non-negative integers A, B, C, D, E, and F, which satisfy A\times B\times C\geq D\times E\times F.  
Find the remainder when (A\times B\times C)-(D\times E\times F) is divided by 998244353.

### Constraints

* 0\leq A,B,C,D,E,F\leq 10^{18}
* A\times B\times C\geq D\times E\times F
* A, B, C, D, E, and F are integers.

---

### Input

The input is given from Standard Input in the following format:

```
A B C D E F
```

### Output

Print the remainder when (A\times B\times C)-(D\times E\times F) is divided by 998244353, as an integer.

---

### Sample Input 1

```
2 3 5 1 2 4
```

### Sample Output 1

```
22
```

Since A\times B\times C=2\times 3\times 5=30 and D\times E\times F=1\times 2\times 4=8,  
we have (A\times B\times C)-(D\times E\times F)=22. Divide this by 998244353 and print the remainder, which is 22.

---

### Sample Input 2

```
1 1 1000000000 0 0 0
```

### Sample Output 2

```
1755647
```

Since A\times B\times C=1000000000 and D\times E\times F=0,  
we have (A\times B\times C)-(D\times E\times F)=1000000000. Divide this by 998244353 and print the remainder, which is 1755647.

---

### Sample Input 3

```
1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000 1000000000000000000
```

### Sample Output 3

```
0
```

We have (A\times B\times C)-(D\times E\times F)=0. Divide this by 998244353 and print the remainder, which is 0.
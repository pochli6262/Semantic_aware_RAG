Score: 150 points

### Problem Statement

You are given N integers A\_1,A\_2,\dots,A\_N, one per line, over N lines. However, **N is not given in the input.**  
Furthermore, the following is guaranteed:

* A\_i \neq 0 ( 1 \le i \le N-1 )
* A\_N = 0

Print A\_N, A\_{N-1},\dots,A\_1 in this order.

### Constraints

* All input values are integers.
* 1 \le N \le 100
* 1 \le A\_i \le 10^9 ( 1 \le i \le N-1 )
* A\_N = 0

---

### Input

The input is given from Standard Input in the following format:

```
A_1
A_2
\vdots
A_N
```

### Output

Print A\_N, A\_{N-1}, \dots, A\_1 in this order, as integers, separated by newlines.

---

### Sample Input 1

```
3
2
1
0
```

### Sample Output 1

```
0
1
2
3
```

Note again that N is not given in the input.
Here, N=4 and A=(3,2,1,0).

---

### Sample Input 2

```
0
```

### Sample Output 2

```
0
```

A=(0).

---

### Sample Input 3

```
123
456
789
987
654
321
0
```

### Sample Output 3

```
0
321
654
987
789
456
123
```
Score : 500 points

### Problem Statement

You are given a permutation P = (P\_1, P\_2, \ldots, P\_N) of (1, 2, \ldots, N).

Print the number of integer sequences A = (A\_1, A\_2, \ldots, A\_N) of length N that satisfy both of the conditions below, modulo 998244353.

* 1 \leq A\_i \leq M for every i = 1, 2, \ldots, N.
* The integer sequence A is lexicographically smaller than the integer sequence (A\_{P\_1}, A\_{P\_2}, \ldots, A\_{P\_N}).

 What is lexicographical order?

An integer sequence X = (X\_1,X\_2,\ldots,X\_N) is  **lexicographically smaller** than an integer sequence Y = (Y\_1,Y\_2,\ldots,Y\_N) when there is an integer 1 \leq i \leq N that satisfies both of the conditions below.

* For all integers j (1 \leq j \leq i-1), X\_j=Y\_j.
* X\_i < Y\_i

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq M \leq 10^9
* 1 \leq P\_i \leq N
* i \neq j \implies P\_i \neq P\_j
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
P_1 P_2 \ldots P_N
```

### Output

Print the number of integer sequences A of length N that satisfy both of the conditions in the Problem Statement, modulo 998244353.

---

### Sample Input 1

```
4 2
4 1 3 2
```

### Sample Output 1

```
6
```

Six integer sequences A satisfy both of the conditions: (1, 1, 1, 2), (1, 1, 2, 2), (1, 2, 1, 2), (1, 2, 2, 2), (2, 1, 1, 2), and (2, 1, 2, 2).  
For instance, when A = (1, 1, 1, 2), we have (A\_{P\_1}, A\_{P\_2}, A\_{P\_3}, A\_{P\_4}) = (2, 1, 1, 1), which is lexicographically larger than A.

---

### Sample Input 2

```
1 1
1
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
20 100000
11 15 3 20 17 6 1 9 5 19 10 16 7 8 12 2 18 14 4 13
```

### Sample Output 3

```
55365742
```
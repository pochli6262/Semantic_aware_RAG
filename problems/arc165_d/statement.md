Score : 700 points

### Problem Statement

For an integer sequence X=(X\_1,X\_2,\dots,X\_n), let X[L,R] denote the integer sequence (X\_L,X\_{L+1},\dots,X\_{R}).

You are given integers N and M, and M quadruples of integers (A\_i,B\_i,C\_i,D\_i).

Determine if there is an integer sequence X of length N that satisfies the following condition for every i=1,2,\dots,M:

* X[A\_i,B\_i] is lexicographically smaller than X[C\_i,D\_i].

 What is lexicographical order on sequences?

A sequence S = (S\_1,S\_2,\ldots,S\_{|S|}) is **lexicographically smaller** than T = (T\_1,T\_2,\ldots,T\_{|T|}) when 1. or 2. below holds.
Here, |S| and |T| denotes the lengths of S and T, respectively.

1. |S| \lt |T| and (S\_1,S\_2,\ldots,S\_{|S|}) = (T\_1,T\_2,\ldots,T\_{|S|}).
2. There is an integer 1 \leq i \leq \min\lbrace |S|, |T| \rbrace that satisfy both of the following:
   * (S\_1,S\_2,\ldots,S\_{i-1}) = (T\_1,T\_2,\ldots,T\_{i-1}).
   * S\_i is smaller than T\_i (as a number).

### Constraints

* 2 \leq N \leq 2000
* 1 \leq M \leq 2000
* 1 \leq A\_i \leq B\_i \leq N
* 1 \leq C\_i \leq D\_i \leq N
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 B_1 C_1 D_1
A_2 B_2 C_2 D_2
\vdots
A_M B_M C_M D_M
```

### Output

If some integer sequence satisfies the condition, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
4 2
1 3 3 4
4 4 1 2
```

### Sample Output 1

```
Yes
```

For example, X=(1,1,2,1) satisfies the condition.

---

### Sample Input 2

```
3 2
1 2 2 3
2 2 1 1
```

### Sample Output 2

```
No
```

No integer sequence X satisfies the condition.

---

### Sample Input 3

```
15 20
2 5 6 14
11 14 10 10
13 15 6 10
8 10 3 8
7 8 1 9
2 8 14 15
14 14 5 12
6 10 9 9
1 4 10 14
5 14 6 7
8 10 5 8
8 10 11 15
4 8 4 11
7 9 1 4
8 10 3 3
11 13 8 14
6 13 4 15
4 7 6 11
2 5 1 2
8 14 6 8
```

### Sample Output 3

```
No
```
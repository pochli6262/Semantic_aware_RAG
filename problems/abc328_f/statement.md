Score : 525 points

### Problem Statement

You are given Q triples of integers (a\_1, b\_1, d\_1), (a\_2, b\_2, d\_2), \ldots, (a\_Q, b\_Q, d\_Q).

A subset S of the set \lbrace 1, 2, \ldots, Q\rbrace is defined to be a **good set** if there exists an integer sequence (X\_1, X\_2, \ldots, X\_N) of length N that satisfies:

> X\_{a\_i} - X\_{b\_i} = d\_i for all i \in S.

Starting with S as an empty set, perform the following operation for i = 1, 2, \ldots, Q in this order:

> If S \cup \lbrace i \rbrace is a good set, then replace S with S \cup \lbrace i \rbrace.

Print all elements of the final set S in **ascending order**.

### Constraints

* All input values are integers.
* 1 \leq N, Q \leq 2 \times 10^5
* 1 \leq a\_i, b\_i \leq N
* -10^9 \leq d\_i \leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N Q
a_1 b_1 d_1
a_2 b_2 d_2
\vdots
a_Q b_Q d_Q
```

### Output

Print the sequence (s\_1, s\_2, \ldots, s\_k) of all elements of the final set S in **ascending order**, separated by spaces, in the following format:

```
s_1 s_2 \ldots s_k
```

---

### Sample Input 1

```
3 5
1 2 2
3 2 -3
2 1 -1
3 3 0
1 3 5
```

### Sample Output 1

```
1 2 4 5
```

Starting with S as an empty set, perform the operation described in the problem statement for i = 1, 2, 3, 4, 5 in this order, as follows.

* For i = 1, the set S \cup \lbrace i \rbrace = \lbrace 1 \rbrace is a good set, because (X\_1, X\_2, X\_3) = (3, 1, 4) satisfies the condition in the problem statement, for example, so replace S with \lbrace 1\rbrace.
* For i = 2, the set S \cup \lbrace i \rbrace = \lbrace 1, 2 \rbrace is a good set, because (X\_1, X\_2, X\_3) = (3, 1, -2) satisfies the condition in the problem statement, for example, so replace S with \lbrace 1, 2\rbrace.
* For i = 3, the set S \cup \lbrace i \rbrace = \lbrace 1, 2, 3 \rbrace is not a good set.
* For i = 4, the set S \cup \lbrace i \rbrace = \lbrace 1, 2, 4 \rbrace is a good set, because (X\_1, X\_2, X\_3) = (3, 1, -2) satisfies the condition in the problem statement, for example, so replace S with \lbrace 1, 2, 4\rbrace.
* For i = 5, the set S \cup \lbrace i \rbrace = \lbrace 1, 2, 4, 5 \rbrace is a good set, because (X\_1, X\_2, X\_3) = (3, 1, -2) satisfies the condition in the problem statement, for example, so replace S with \lbrace 1, 2, 4, 5\rbrace.

Therefore, the final set S is \lbrace 1, 2, 4, 5\rbrace.

---

### Sample Input 2

```
200000 1
1 1 1
```

### Sample Output 2

```

```

The final set S is empty.

---

### Sample Input 3

```
5 20
4 2 125421359
2 5 -191096267
3 4 -42422908
3 5 -180492387
3 3 174861038
2 3 -82998451
3 4 -134761089
3 1 -57159320
5 2 191096267
2 4 -120557647
4 2 125421359
2 3 142216401
4 5 -96172984
3 5 -108097816
1 5 -50938496
1 2 140157771
5 4 65674908
4 3 35196193
4 4 0
3 4 188711840
```

### Sample Output 3

```
1 2 3 6 8 9 11 14 15 16 17 19
```
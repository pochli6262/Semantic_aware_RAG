Score: 525 points

### Problem Statement

There are N people, numbered 1 to N.

A competition was held among these N people, and they were ranked accordingly. The following information is given about their ranks:

* Each person has a unique rank.
* For each 1 \leq i \leq M, if person A\_i is ranked x-th and person B\_i is ranked y-th, then x - y = C\_i.

The given input guarantees that there is at least one possible ranking that does not contradict the given information.

Answer N queries. The answer to the i-th query is an integer determined as follows:

* If the rank of person i can be uniquely determined, return that rank. Otherwise, return -1.

### Constraints

* 2 \leq N \leq 16
* 0 \leq M \leq \frac{N(N - 1)}{2}
* 1 \leq A\_i, B\_i \leq N
* 1 \leq C\_i \leq N - 1
* (A\_i, B\_i) \neq (A\_j, B\_j) (i \neq j)
* There is at least one possible ranking that does not contradict the given information.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 B_1 C_1
A_2 B_2 C_2
\vdots
A_M B_M C_M
```

### Output

Print the answers to the 1-st, 2-nd, \ldots, N-th queries in this order, separated by spaces.

---

### Sample Input 1

```
5 2
2 3 3
5 4 3
```

### Sample Output 1

```
3 -1 -1 -1 -1
```

Let X\_i be the rank of person i. Then, (X\_1, X\_2, X\_3, X\_4, X\_5) could be (3, 4, 1, 2, 5) or (3, 5, 2, 1, 4).

Therefore, the answer to the 1-st query is 3, and the answers to the 2-nd, 3-rd, 4-th, and 5-th queries are -1.

---

### Sample Input 2

```
3 0
```

### Sample Output 2

```
-1 -1 -1
```

---

### Sample Input 3

```
8 5
6 7 3
8 1 7
4 5 1
7 2 1
6 2 4
```

### Sample Output 3

```
1 -1 -1 -1 -1 -1 -1 8
```
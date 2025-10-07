Score : 500 points

### Problem Statement

We have a number sequence A = (A\_1, A\_2, \dots, A\_N) of length N and integers X and Y.
Find the number of pairs of integers (L, R) satisfying all the conditions below.

* 1 \leq L \leq R \leq N
* The maximum value of A\_L, A\_{L+1}, \dots, A\_R is X, and the minimum is Y.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq A\_i \leq 2 \times 10^5
* 1 \leq Y \leq X \leq 2 \times 10^5
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N X Y
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 3 1
1 2 3 1
```

### Sample Output 1

```
4
```

4 pairs satisfy the conditions: (L,R)=(1,3),(1,4),(2,4),(3,4).

---

### Sample Input 2

```
5 2 1
1 3 2 4 1
```

### Sample Output 2

```
0
```

No pair (L,R) satisfies the condition.

---

### Sample Input 3

```
5 1 1
1 1 1 1 1
```

### Sample Output 3

```
15
```

It may hold that X=Y.

---

### Sample Input 4

```
10 8 1
2 7 1 8 2 8 1 8 2 8
```

### Sample Output 4

```
36
```
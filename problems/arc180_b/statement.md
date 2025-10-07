Score : 600 points

### Problem Statement

You are given a permutation P=(P\_1,P\_2,\cdots,P\_N) of (1,2,\cdots,N).
Additionally, you are given an integer K.

You can perform the following operation zero or more times:

* Choose integers l and r (1 \leq l < r \leq N). Here, the pair (l,r) must satisfy all of the following conditions:
  + K \leq r-l.
  + P\_l > P\_r at the time of the operation.
  + The pair (l,r) has never been chosen before.
* Then, swap the values of P\_l and P\_r.

You want to maximize the number of operations.
Find one way to achieve this.

### Constraints

* 2 \leq N \leq 500
* 1 \leq K \leq N-1
* (P\_1,P\_2,\cdots,P\_N) is a permutation of (1,2,\cdots,N).
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K
P_1 P_2 \cdots P_N
```

### Output

Print the answer in the following format:

```
m
l_1 r_1
l_2 r_2
\vdots
l_m r_m
```

Here, m is the maximum number of operations, and l\_i and r\_i are the values of l and r chosen in the i-th operation, respectively.
If multiple solutions exist, you can print any of them.

---

### Sample Input 1

```
3 1
3 2 1
```

### Sample Output 1

```
3
2 3
1 3
1 2
```

In this example, the maximum number of operations is 3.
The operations in the sample output proceed as follows:

* 1st operation: Choose (l,r)=(2,3). We have 1 \leq 3-2 and P\_2 > P\_3, and (2,3) has not been chosen before, so the conditions are satisfied. Swap P\_2 and P\_3, resulting in P=(3,1,2).
* 2nd operation: Choose (l,r)=(1,3). We have 1 \leq 3-1 and P\_1 > P\_3, and (1,3) has not been chosen before, so the conditions are satisfied. Swap P\_1 and P\_3, resulting in P=(2,1,3).
* 3rd operation: Choose (l,r)=(1,2). We have 1 \leq 2-1 and P\_1 > P\_2, and (1,2) has not been chosen before, so the conditions are satisfied. Swap P\_1 and P\_2, resulting in P=(1,2,3).

---

### Sample Input 2

```
5 4
1 4 3 2 5
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
4 2
4 1 2 3
```

### Sample Output 3

```
2
1 4
1 3
```

---

### Sample Input 4

```
10 5
8 7 6 10 9 3 1 5 2 4
```

### Sample Output 4

```
15
3 8
2 8
3 10
3 9
1 8
2 10
2 9
2 7
1 10
5 10
1 9
4 10
4 9
1 7
1 6
```
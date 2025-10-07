Score : 400 points

### Problem Statement

You are given an integer sequence of length N: A=(A\_1,A\_2,\dots,A\_N). You can perform the following operation any number of times (possibly zero).

* Choose an integer i such that 1 \le i \le N, and increase or decrease A\_i by 1.

Your goal is to make at least M integers i(3 \le i \le N) satisfy A\_1 \le A\_i \le A\_2. Find the minimum number of operations required to achieve this goal.

### Constraints

* 3 \le N \le 2 \times 10^5
* 1 \le M \le N-2
* 1 \le A\_i \le 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 A_2 \dots A_N
```

### Output

Print the minimum number of operations required.

---

### Sample Input 1

```
3 1
2 3 5
```

### Sample Output 1

```
2
```

You can make not less than one integer i(3 \le i \le N) satisfy A\_1 \le A\_i \le A\_2 by performing the operation as follows.

* Choose i=3, and decrease A\_i by 1.
* Choose i=2, and increase A\_i by 1.

Since it is impossible to achieve the goal with less than 2 operation, the answer is 2.

---

### Sample Input 2

```
5 2
1 4 2 3 5
```

### Sample Output 2

```
0
```

You may already have achieved the goal from the start.

---

### Sample Input 3

```
8 5
15 59 64 96 31 17 88 9
```

### Sample Output 3

```
35
```
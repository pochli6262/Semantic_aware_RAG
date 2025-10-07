Score : 500 points

### Problem Statement

You are given a permutation P=(P\_1,P\_2,\ldots,P\_N) of (1,2,\ldots,N).

You can repeat the following two kinds of operations in any order to make P sorted in increasing order.

* Operation A: Choose an integer i such that 1 \leq i \leq N-1, and swap P\_i and P\_{i+1}.
* Operation B: Choose an integer i such that 1 \leq i \leq N-2, and swap P\_i and P\_{i+2}.

Find a sequence of operations with the following property:

* The number of Operations A is the minimum possible.
* The total number of operations is not larger than 10^5.

Under the Constraints of this problem, we can prove that a solution always exists.

### Constraints

* 2 \leq N \leq 400
* 1 \leq P\_i \leq N \,(1 \leq i \leq N)
* P\_i \neq P\_j \,(1 \leq i < j \leq N)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
P_1 P_2 \ldots P_N
```

### Output

Let S be the number of operations in your answer.
Print S+1 lines.

The first line should contain S.

The (s+1)-th (1 \leq s \leq S) line should contain the following:

* `A i` if the s-th operation is Operation A, and the integer chosen in this operation is i.
* `B i` if the s-th operation is Operation B, and the integer chosen in this operation is i.

If there are multiple solutions satisfying the condition, printing any of them will be accepted.

---

### Sample Input 1

```
4
3 2 4 1
```

### Sample Output 1

```
4
A 3
B 1
B 2
B 2
```

In this Sample Output, P changes like this: (3,2,4,1) \rightarrow (3,2,1,4) \rightarrow (1,2,3,4) \rightarrow (1,4,3,2) \rightarrow (1,2,3,4).

Note that you don't have to minimize the total number of operations.

---

### Sample Input 2

```
3
1 2 3
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
6
2 1 4 3 6 5
```

### Sample Output 3

```
3
A 1
A 3
A 5
```
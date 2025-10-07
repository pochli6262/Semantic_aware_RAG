Score : 600 points

### Problem Statement

Blocks are stacked in a triangle. The i-th column from the top has i blocks.

You are given a sequence P = ((a\_1, c\_1), (a\_2, c\_2), ..., (a\_M, c\_M)) which is a result of the run-length compression of a sequence A = (A\_1, A\_2, ..., A\_N) consisting of non-negative integers less than or equal to 6.

* For example, when A = (2, 2, 2, 5, 5, 1), you are given P = ((2, 3), (5, 2), (1, 1)).

You will write a number on each block so that the following conditions are satisfied, where B\_{i,j} denotes the number to write on the j-th block from the left in the i-th column from the top:

* For all integers i such that 1 \leq i \leq N, it holds that B\_{N,i} = A\_{i}.
* For all pairs of integers (i, j) such that 1 \leq j \leq i \leq N-1, it holds that B\_{i,j}= (B\_{i+1,j}+B\_{i+1,j+1})\bmod 7.

Enumerate the numbers written on the blocks in the K-th column from the top.

What is run-length compression?
The run-length compression is a conversion from a given sequence A to a sequence of pairs of integers obtained by the following procedure.

1. Split A off at the positions where two different elements are adjacent to each other.
2. For each subsequence B that has been split off, replace B with a integer pair of "the number which B consists of" and "the length of B".- Construct a sequence consisting of the integer pairs after the replacement without changing the order.

### Constraints

* 1 \leq N \leq 10^9
* 1 \leq M \leq \min(N, 200)
* 1 \leq K \leq \min(N,5 \times 10^5)
* 0 \leq a\_i \leq 6
* 1 \leq c\_i \leq N
* \sum\_{i=1}^M c\_i = N
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M K
a_1 c_1
a_2 c_2
\vdots
a_M c_M
```

### Output

Print the answer in the following format. It is guaranteed that the answer is unique under the Constraint of the problem.

```
B_{K,1} B_{K,2} \dots B_{K,K}
```

---

### Sample Input 1

```
6 3 4
2 3
5 2
1 1
```

### Sample Output 1

```
1 4 3 2
```

We have A = (2,2,2,5,5,1). The number written on the blocks are as follows.

```
     3
    5 5
   5 0 5
  1 4 3 2
 4 4 0 3 6
2 2 2 5 5 1
```

---

### Sample Input 2

```
1 1 1
6 1
```

### Sample Output 2

```
6
```

---

### Sample Input 3

```
111111111 9 9
0 1
1 10
2 100
3 1000
4 10000
5 100000
6 1000000
0 10000000
1 100000000
```

### Sample Output 3

```
1 0 4 2 5 5 5 6 3
```
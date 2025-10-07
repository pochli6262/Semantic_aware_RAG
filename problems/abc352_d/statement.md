Score: 425 points

### Problem Statement

You are given a permutation P = (P\_1, P\_2, \dots, P\_N) of (1, 2, \dots, N).

A length-K sequence of indices (i\_1, i\_2, \dots, i\_K) is called a **good index sequence** if it satisfies both of the following conditions:

* 1 \leq i\_1 < i\_2 < \dots < i\_K \leq N.
* The subsequence (P\_{i\_1}, P\_{i\_2}, \dots, P\_{i\_K}) can be obtained by rearranging some consecutive K integers.
    
  Formally, there exists an integer a such that \lbrace P\_{i\_1},P\_{i\_2},\dots,P\_{i\_K} \rbrace = \lbrace a,a+1,\dots,a+K-1 \rbrace.

Find the minimum value of i\_K - i\_1 among all good index sequences. It can be shown that at least one good index sequence exists under the constraints of this problem.

### Constraints

* 1 \leq K \leq N \leq 2 \times 10^5
* 1 \leq P\_i \leq N
* P\_i \neq P\_j if i \neq j.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K
P_1 P_2 \dots P_N
```

### Output

Print the minimum value of i\_K - i\_1 among all good index sequences.

---

### Sample Input 1

```
4 2
2 3 1 4
```

### Sample Output 1

```
1
```

The good index sequences are (1,2),(1,3),(2,4). For example, (i\_1, i\_2) = (1,3) is a good index sequence because 1 \leq i\_1 < i\_2 \leq N and (P\_{i\_1}, P\_{i\_2}) = (2,1) is a rearrangement of two consecutive integers 1, 2.

Among these good index sequences, the smallest value of i\_K - i\_1 is for (1,2), which is 2-1=1.

---

### Sample Input 2

```
4 1
2 3 1 4
```

### Sample Output 2

```
0
```

i\_K - i\_1 = i\_1 - i\_1 = 0 in all good index sequences.

---

### Sample Input 3

```
10 5
10 1 6 8 7 2 5 9 3 4
```

### Sample Output 3

```
5
```
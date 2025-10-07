Score : 600 points

### Problem Statement

You are given a string S = s\_1 s\_2 \ldots s\_N of length N consisting of 0's and 1's.

Find the maximum integer K such that there is a sequence of K pairs of integers \big((L\_1, R\_1), (L\_2, R\_2), \ldots, (L\_K, R\_K)\big) that satisfy all three conditions below.

* 1 \leq L\_i \leq R\_i \leq N for each i = 1, 2, \ldots, K.
* R\_i \lt L\_{i+1} for i = 1, 2, \ldots, K-1.
* The string s\_{L\_i}s\_{L\_i+1} \ldots s\_{R\_i} is **strictly lexicographically smaller** than the string s\_{L\_{i+1}}s\_{L\_{i+1}+1}\ldots s\_{R\_{i+1}}.

### Constraints

* 1 \leq N \leq 2.5 \times 10^4
* N is an integer.
* S is a string of length N consisting of 0's and 1's.

---

### Input

Input is given from Standard Input in the following format:

```
N
S
```

### Output

Print the answer.

---

### Sample Input 1

```
7
0101010
```

### Sample Output 1

```
3
```

For K = 3, one sequence satisfying the conditition is (L\_1, R\_1) = (1, 1), (L\_2, R\_2) = (3, 5), (L\_3, R\_3) = (6, 7).
Indeed, s\_1 = 0 is strictly lexicographically smaller than s\_3s\_4s\_5 = 010, and s\_3s\_4s\_5 = 010 is strictly lexicographically smaller than s\_6s\_7 = 10.  
For K \geq 4, there is no sequence \big((L\_1, R\_1), (L\_2, R\_2), \ldots, (L\_K, R\_K)\big) satisfying the condition.

---

### Sample Input 2

```
30
000011001110101001011110001001
```

### Sample Output 2

```
9
```
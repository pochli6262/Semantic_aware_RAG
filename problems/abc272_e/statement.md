Score : 500 points

### Problem Statement

You are given an integer sequence A=(A\_1,A\_2,\ldots,A\_N) of length N.

Perform the following operation M times:

* For each i\ (1\leq i \leq N), add i to A\_i. Then, find the minimum non-negative integer not contained in A.

### Constraints

* 1\leq N,M \leq 2\times 10^5
* -10^9\leq A\_i\leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M 
A_1 A_2 \ldots A_N
```

### Output

Print M lines.

The i-th (1\leq i \leq M) line should contain the minimum non-negative integer not contained in A after the i-th operation.

---

### Sample Input 1

```
3 3
-1 -1 -6
```

### Sample Output 1

```
2
2
0
```

The 1-st operation makes the sequence A

(-1 + 1, -1 +2 ,-6+3) = (0,1,-3).

The minimum non-negative integer not contained in A is 2.

The 2-nd operation makes the sequence A

(0 + 1, 1 +2 ,-3+3) = (1,3,0).

The minimum non-negative integer not contained in A is 2.

The 3-rd operation makes the sequence A

(1 + 1, 3 +2 ,0+3) = (2,5,3).

The minimum non-negative integer not contained in A is 0.

---

### Sample Input 2

```
5 6
-2 -2 -5 -7 -15
```

### Sample Output 2

```
1
3
2
0
0
0
```
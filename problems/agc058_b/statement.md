Score : 700 points

### Problem Statement

You are given a permutation P=(P\_1,P\_2,\cdots,P\_N) of (1,2,\cdots,N).

You may perform the following operation zero or more times.

* Choose an integer i (1 \leq i \leq N-1).
  Let v=\max(P\_i,P\_{i+1}) and replace the values of P\_i and P\_{i+1} with v.

How many sequences are there that P can be after your operations? Find the count modulo 998244353.

### Constraints

* 2 \leq N \leq 5000
* (P\_1,P\_2,\cdots,P\_N) is a permutation of (1,2,\cdots,N).
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
P_1 P_2 \cdots P_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
1 3 2
```

### Sample Output 1

```
4
```

The four sequences that P can become are (1,3,2), (3,3,2), (1,3,3), and (3,3,3).

---

### Sample Input 2

```
4
2 1 3 4
```

### Sample Output 2

```
11
```

---

### Sample Input 3

```
10
4 9 6 3 8 10 1 2 7 5
```

### Sample Output 3

```
855
```
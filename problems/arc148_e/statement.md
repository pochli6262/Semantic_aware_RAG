Score : 800 points

### Problem Statement

You are given a sequence of length N, A = (A\_1, ..., A\_N), and an integer K.  
How many permutations of A are there such that no two adjacent elements sum to less than K? Find the count modulo 998244353.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 0 \leq K \leq 10^9
* 0 \leq A\_i \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 5
1 2 3 4
```

### Sample Output 1

```
4
```

The following four permutations satisfy the condition:

* (1, 4, 2, 3)
* (1, 4, 3, 2)
* (2, 3, 4, 1)
* (3, 2, 4, 1)

---

### Sample Input 2

```
4 3
1 2 3 3
```

### Sample Output 2

```
12
```

There are 12 permutations of A, all of which satisfy the condition.

---

### Sample Input 3

```
10 7
3 1 4 1 5 9 2 6 5 3
```

### Sample Output 3

```
108
```
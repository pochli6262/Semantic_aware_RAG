Score : 600 points

### Problem Statement

You are given an integer sequence A = (A\_1, \dots, A\_N) of length N.

Find the number, modulo 998244353, of permutations P = (P\_1, \dots, P\_N) of (1, 2, \dots, N) such that:

* there exist exactly K integers i between 1 and (N-1) (inclusive) such that A\_{P\_i} \lt A\_{P\_{i + 1}}.

### Constraints

* 2 \leq N \leq 5000
* 0 \leq K \leq N - 1
* 1 \leq A\_i \leq N \, (1 \leq i \leq N)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N K
A_1 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2
1 1 2 2
```

### Sample Output 1

```
4
```

Four permutations satisfy the condition: P = (1, 3, 2, 4), (1, 4, 2, 3), (2, 3, 1, 4), (2, 4, 1, 3).

---

### Sample Input 2

```
10 3
3 1 4 1 5 9 2 6 5 3
```

### Sample Output 2

```
697112
```
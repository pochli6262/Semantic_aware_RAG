Score : 650 points

### Problem Statement

> The definition of a good pair of sequences in this problem is the same as in Problem D.

A pair of sequences of length M consisting of positive integers at most N, (S, T) = ((S\_1, S\_2, \dots, S\_M), (T\_1, T\_2, \dots, T\_M)), is said to **be a good pair of sequences** when (S, T) satisfies the following condition.

* There exists a sequence X = (X\_1, X\_2, \dots, X\_N) of length N consisting of 0 and 1 that satisfies the following condition:
  + X\_{S\_i} \neq X\_{T\_i} for each i=1, 2, \dots, M.

Among the N^{2M} possible pairs of sequences of length M consisting of positive integers at most N, (A, B) = ((A\_1, A\_2, \dots, A\_M), (B\_1, B\_2, \dots, B\_M)), find the number, modulo 998244353, of those that are good pairs of sequences.

### Constraints

* 1 \leq N \leq 30
* 1 \leq M \leq 10^9
* N and M are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
```

### Output

Print the number, modulo 998244353, of pairs of sequences of length M consisting of positive integers at most N that are good pairs of sequences.

---

### Sample Input 1

```
3 2
```

### Sample Output 1

```
36
```

For example, if A=(1,2), B=(2,3), then (A, B) is a good pair of sequences. Indeed, if we set X=(0,1,0), then X is a sequence of length N consisting of 0 and 1 that satisfies X\_{A\_1} \neq X\_{B\_1} and X\_{A\_2} \neq X\_{B\_2}. Thus, (A, B) satisfies the condition of being a good pair of sequences.  
There are a total of 36 good pairs of sequences, so print this number.

---

### Sample Input 2

```
3 3
```

### Sample Output 2

```
168
```

---

### Sample Input 3

```
12 34
```

### Sample Output 3

```
539029838
```

---

### Sample Input 4

```
20 231104
```

### Sample Output 4

```
966200489
```
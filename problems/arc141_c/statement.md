Score : 600 points

### Problem Statement

A string of length 2N, S=S\_1S\_2\dots S\_{2N}, is said to be a *parenthesis sequence* when S is composed of N `(`s and N `)`s.

Additionally, a parenthesis sequence S is said to be *correct* when it is one of the following.

* An empty string.
* The concatenation of `(`, A, `)` in this order, where A is a correct parenthesis sequence.
* The concatenation of A, B in this order, where A and B are non-empty correct parenthesis sequences.

You are given two permutations P=(P\_1,\ P\_2,\ \dots,\ P\_{2N}) and Q=(Q\_1,\ Q\_2,\ \dots,\ Q\_{2N}) of the integers from 1 to 2N.

Determine whether there exists a parenthesis sequence S=S\_1S\_2\dots S\_{2N} that satisfies the following conditions.

* P is the lexicographically smallest permutation p of the integers from 1 to 2N such that S\_{p\_1}S\_{p\_2}\dots S\_{p\_{2N}} is a correct parenthesis sequence.
* Q is the lexicographically largest permutation p of the integers from 1 to 2N such that S\_{p\_1}S\_{p\_2}\dots S\_{p\_{2N}} is a correct parenthesis sequence.

If such a parenthesis sequence exists, find one.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq P\_i,Q\_i \leq 2N
* Each of P and Q is a permutation of 1 to 2N.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
P_1 P_2 \dots P_{2N}
Q_1 Q_2 \dots Q_{2N}
```

### Output

If there exists a parenthesis sequence S that satisfies the conditions above, print one such sequence. If there are multiple such sequences, you may print any of them.

If there is no such sequence, print `-1`.

---

### Sample Input 1

```
2
1 2 4 3
4 3 1 2
```

### Sample Output 1

```
())(
```

For S= `())(`, some of the permutations p such that S\_{p\_1}S\_{p\_2}S\_{p\_3}S\_{p\_4} is a correct parenthesis sequence are p=(1,\ 4,\ 2,\ 3),\ (1,\ 4,\ 3,\ 2). The lexicographically smallest and largest among them are p=(1,\ 2,\ 4,\ 3) and p=(4,\ 3,\ 1,\ 2), satisfying the conditions.

---

### Sample Input 2

```
2
1 3 2 4
4 3 2 1
```

### Sample Output 2

```
-1
```

No S satisfies the conditions.

---

### Sample Input 3

```
3
2 1 5 3 4 6
6 5 3 4 2 1
```

### Sample Output 3

```
-1
```
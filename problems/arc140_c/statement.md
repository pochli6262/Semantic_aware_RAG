Score : 500 points

### Problem Statement

The **happiness** of a permutation P=(P\_1,P\_2,\ldots,P\_N) of (1,\dots,N) is defined as follows.

* Let A=(A\_1,A\_2,\ldots,A\_{N-1}) be a sequence of length N-1 with A\_i = |P\_i-P\_{i+1}|(1\leq i \leq N-1). The happiness of P is the length of a longest strictly increasing subsequence of A.

Print a permutation P such that P\_1 = X with the greatest happiness.

### Constraints

* 2 \leq N \leq 2\times 10^5
* 1 \leq X \leq N
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N X
```

### Output

Print a permutation P such that P\_1 = X with the greatest happiness, in the following format:

```
P_1 P_2 \ldots P_N
```

If there are multiple solutions, printing any of them will be accepted.

---

### Sample Input 1

```
3 2
```

### Sample Output 1

```
2 1 3
```

Since A=(1,2), the happiness of P is 2, which is the greatest happiness achievable, so the output meets the requirement.

---

### Sample Input 2

```
3 1
```

### Sample Output 2

```
1 2 3
```

Since A=(1,1), the happiness of P is 1, which is the greatest happiness achievable, so the output meets the requirement.
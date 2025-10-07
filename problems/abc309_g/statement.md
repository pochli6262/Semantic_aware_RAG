Score : 575 points

### Problem Statement

Find the number, modulo 998244353, of permutations P=(P\_1,P\_2,\dots,P\_N) of (1,2,\dots,N) such that:

* |P\_i - i| \ge X for all integers i with 1 \le i \le N.

### Constraints

* 1 \le N \le 100
* 1 \le X \le 5
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N X
```

### Output

Print the answer.

---

### Sample Input 1

```
3 1
```

### Sample Output 1

```
2
```

The conforming permutations P=(P\_1,P\_2,P\_3) are the following two, (2,3,1) and (3,1,2), so the answer is 2.

---

### Sample Input 2

```
5 2
```

### Sample Output 2

```
4
```

---

### Sample Input 3

```
98 5
```

### Sample Output 3

```
809422418
```
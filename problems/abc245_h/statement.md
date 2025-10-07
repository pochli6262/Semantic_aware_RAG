Score : 600 points

### Problem Statement

Among the sequences of length K consisting of integers, A=(A\_1, \ldots, A\_K), how many satisfy all of the conditions below?  
Find the count modulo 998244353.

* 0\leq A\_i \leq M-1 for every i(1\leq i\leq K).
* \displaystyle\prod\_{i=1}^{K} A\_i \equiv N \pmod M.

### Constraints

* 1 \leq K \leq 10^9
* 0 \leq N \lt M \leq 10^{12}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
K N M
```

### Output

Print the answer.

---

### Sample Input 1

```
2 3 6
```

### Sample Output 1

```
5
```

The five sequences A satisfying the conditions are (1,3),(3,1),(3,3),(3,5),(5,3).

---

### Sample Input 2

```
10 0 2
```

### Sample Output 2

```
1023
```

---

### Sample Input 3

```
1000000000 20220326 1000000000000
```

### Sample Output 3

```
561382653
```

Be sure to find the count modulo 998244353.
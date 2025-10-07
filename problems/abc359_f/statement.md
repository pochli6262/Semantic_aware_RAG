Score : 550 points

### Problem Statement

You are given a sequence of integers A=(A\_1,\ldots,A\_N). For a tree T with N vertices, define f(T) as follows:

* Let d\_i be the degree of vertex i in T. Then, f(T)=\sum\_{i=1}^N {d\_i}^2 A\_i.

Find the minimum possible value of f(T).

The constraints guarantee the answer to be less than 2^{63}.

### Constraints

* 2\leq N\leq 2\times 10^5
* 1\leq A\_i \leq 10^9
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N 
A_1 A_2 \ldots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4
3 2 5 2
```

### Sample Output 1

```
24
```

Consider a tree T with an edge connecting vertices 1 and 2, an edge connecting vertices 2 and 4, and an edge connecting vertices 4 and 3.

Then, f(T) = 1^2\times 3 + 2^2\times 2 + 1^2\times 5 + 2^2\times 2 = 24. It can be proven that this is the minimum value of f(T).

---

### Sample Input 2

```
3
4 3 2
```

### Sample Output 2

```
15
```

---

### Sample Input 3

```
7
10 5 10 2 10 13 15
```

### Sample Output 3

```
128
```
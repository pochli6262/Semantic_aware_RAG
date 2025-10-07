Score : 600 points

### Problem Statement

For a sequence of length N, A = (A\_1,A\_2,\dots,A\_N), consisting of integers between 1 and N, inclusive, and an integer i\ (1\leq i \leq N), let us define a sequence of length 10^{100}, B\_i=(B\_{i,1},B\_{i,2},\dots,B\_{i,10^{100}}), as follows.

* B\_{i,1}=i.
* B\_{i,j+1}=A\_{B\_{i,j}}\ (1\leq j<10^{100}).

Additionally, let us define S\_i as the number of distinct integers that occur exactly once in the sequence B\_i.
More formally, S\_i is the number of values k such that exactly one index j\ (1\leq j\leq 10^{100}) satisfies B\_{i,j}=k.

You are given an integer N. There are N^N sequences that can be A. Find the sum of \displaystyle \sum\_{i=1}^{N} S\_i over all of them, modulo M.

### Constraints

* 1\leq N \leq 2\times 10^5
* 10^8\leq M \leq 10^9
* N and M are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
4 100000000
```

### Sample Output 1

```
624
```

As an example, let us consider the case A=(2,3,3,4).

* For i=1: we have B\_1=(1,2,3,3,3,\dots), where two integers, 1 and 2, occur exactly once, so S\_1=2.
* For i=2: we have B\_2=(2,3,3,3,\dots), where one integer, 2, occurs exactly once, so S\_2=1.
* For i=3: we have B\_3=(3,3,3,\dots), where no integers occur exactly once, so S\_3=0.
* For i=4: we have B\_4=(4,4,4,\dots), where no integers occur exactly once, so S\_4=0.

Thus, we have \displaystyle \sum\_{i=1}^{N} S\_i=2+1+0+0=3.

If we similarly compute \displaystyle \sum\_{i=1}^{N} S\_i for the other 255 sequences, the sum of this value over all 256 sequences is 624.

---

### Sample Input 2

```
7 1000000000
```

### Sample Output 2

```
5817084
```

---

### Sample Input 3

```
2023 998244353
```

### Sample Output 3

```
737481389
```

Print the sum modulo M.

---

### Sample Input 4

```
100000 353442899
```

### Sample Output 4

```
271798911
```
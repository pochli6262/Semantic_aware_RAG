Score : 500 points

### Problem Statement

We have an integer sequence of length N: x=(x\_0,x\_1,\cdots,x\_{N-1}) (note that its index is 0-based).
Initially, all elements of x are 0.

You can repeat the following operation any number of times.

* Choose integers i,k (0 \leq i \leq N-1, 1 \leq k \leq N).
  Then, for every j such that i \leq j \leq i+k-1, increase the value of x\_{j\bmod N} by 1.

You are given an integer sequence of length N: A=(A\_0,A\_1,\cdots,A\_{N-1}).
Find the minimum number of operations needed to make x equal A.

### Constraints

* 1 \leq N \leq 200000
* 1 \leq A\_i \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_0 A_1 \cdots A_{N-1}
```

### Output

Print the answer.

---

### Sample Input 1

```
4
1 2 1 2
```

### Sample Output 1

```
2
```

We should do the following.

* Initially, we have x=(0,0,0,0).
* Do the operation with i=1,k=3, making x=(0,1,1,1).
* Do the operation with i=3,k=3, making x=(1,2,1,2).

---

### Sample Input 2

```
5
3 1 4 1 5
```

### Sample Output 2

```
7
```

---

### Sample Input 3

```
1
1000000000
```

### Sample Output 3

```
1000000000
```
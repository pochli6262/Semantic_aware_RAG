Score : 600 points

### Problem Statement

We have a sequence X, which is initially empty.  
Takahashi has performed the following operation for i=1,2,\ldots,N in this order.

* Append l\_i,l\_i+1,\ldots,r\_i in this order to the end of X.

Find the greatest length of a strictly increasing subsequence of the final X.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq l\_i \leq r\_i \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
l_1 r_1
\vdots
l_{N} r_{N}
```

### Output

Print the answer.

---

### Sample Input 1

```
4
1 1
2 4
10 11
7 10
```

### Sample Output 1

```
8
```

The final X is (1,2,3,4,10,11,7,8,9,10).  
The 1-st, 2-nd, 3-rd, 4-th, 7-th, 8-th, 9-th, and 10-th elements form a strictly increasing subsequence with the greatest length.

---

### Sample Input 2

```
4
1 1
1 1
1 1
1 1
```

### Sample Output 2

```
1
```

The final X is (1,1,1,1).

---

### Sample Input 3

```
1
1 1000000000
```

### Sample Output 3

```
1000000000
```
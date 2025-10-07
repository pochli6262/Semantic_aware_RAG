Score : 400 points

### Problem Statement

There is a sequence that contains one 0, A=(0).  
Additionally, you are given a string of length N, S=s\_1s\_2\ldots s\_N, consisting of `L` and `R`.

For each i=1, 2, \ldots, N in this order, the following will be done.

* If s\_i is `L`, insert i to the immediate left of i-1 in A.
* If s\_i is `R`, insert i to the immediate right of i-1 in A.

Find the final contents of A.

### Constraints

* 1\leq N \leq 5\times 10^5
* N is an integer.
* |S| = N
* s\_i is `L` or `R`.

---

### Input

Input is given from Standard Input in the following format:

```
N
S
```

### Output

Print the final contents of A, separated by spaces.

---

### Sample Input 1

```
5
LRRLR
```

### Sample Output 1

```
1 2 4 5 3 0
```

Initially, A=(0).  
S\_1 is `L`, which makes it A=(1,0).  
S\_2 is `R`, which makes it A=(1,2,0).  
S\_3 is `R`, which makes it A=(1,2,3,0).  
S\_4 is `L`, which makes it A=(1,2,4,3,0).  
S\_5 is `R`, which makes it A=(1,2,4,5,3,0).

---

### Sample Input 2

```
7
LLLLLLL
```

### Sample Output 2

```
7 6 5 4 3 2 1 0
```
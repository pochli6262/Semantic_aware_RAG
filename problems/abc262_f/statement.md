Score : 500 points

### Problem Statement

You are given a sequence P = (p\_1,p\_2,\ldots,p\_N) that contains 1,2,\ldots,N exactly once each.  
You may perform the following operations between 0 and K times in total in any order:

* Choose one term of P and remove it.
* Move the last term of P to the head.

Find the lexicographically smallest P that can be obtained as a result of the operations.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 0 \leq K \leq N-1
* 1 \leq p\_i \leq N
* (p\_1,p\_2,\ldots,p\_N) contains 1,2,\ldots,N exactly once each.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N K
p_1 p_2 \ldots p_N
```

### Output

Print the lexicographically smallest P that can be obtained as a result of the operations, separated by spaces.

---

### Sample Input 1

```
5 3
4 5 2 3 1
```

### Sample Output 1

```
1 2 3
```

The following operations make P equal (1,2,3).

* Removing the first term makes P equal (5,2,3,1).
* Moving the last term to the head makes P equal (1,5,2,3).
* Removing the second term makes P equal (1,2,3).

There is no way to obtain P lexicographically smaller than (1,2,3), so this is the answer.

---

### Sample Input 2

```
3 0
3 2 1
```

### Sample Output 2

```
3 2 1
```

You may be unable to perform operations.

---

### Sample Input 3

```
15 10
12 10 7 2 8 11 9 1 6 14 3 15 13 5 4
```

### Sample Output 3

```
1 3 4 7 2 8 11 9
```
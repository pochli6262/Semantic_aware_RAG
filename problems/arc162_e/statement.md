Score : 700 points

### Problem Statement

You are given a sequence of length N consisting of integers from 1 to N, A=(A\_1,A\_2,\ldots,A\_N).

Find the number, modulo 998244353, of sequences of length N consisting of integers from 1 to N, B=(B\_1,B\_2,\ldots,B\_N), that satisfy the following conditions for all i=1,2,\ldots,N.

* The number of occurrences of i in B is at most A\_i.
* The number of occurrences of B\_i in B is at most A\_i.

### Constraints

* 1 \leq N \leq 500
* 1 \leq A\_i \leq N
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
3
1 2 3
```

### Sample Output 1

```
10
```

The following 10 sequences satisfy the conditions:

* (1,2,2)
* (1,2,3)
* (1,3,2)
* (1,3,3)
* (2,1,3)
* (2,3,1)
* (2,3,3)
* (3,1,2)
* (3,2,1)
* (3,2,2)

---

### Sample Input 2

```
4
4 4 4 4
```

### Sample Output 2

```
256
```

All sequences of length 4 consisting of integers from 1 to 4 satisfy the conditions, and there are 4^4=256 such sequences.

---

### Sample Input 3

```
5
1 1 1 1 1
```

### Sample Output 3

```
120
```

All permutations of (1,2,3,4,5) satisfy the conditions, and there are 5!=120 such sequences.

---

### Sample Input 4

```
14
6 5 14 3 6 7 3 11 11 2 3 7 8 10
```

### Sample Output 4

```
628377683
```

Be sure to print the number modulo 998244353.
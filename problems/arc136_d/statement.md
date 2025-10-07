Score : 600 points

### Problem Statement

You are given an integer sequence of length N: A=(A\_1,A\_2,\cdots,A\_N).

Find the number of pairs of integers (i,j) (1 \leq i < j \leq N) such that calculation of A\_i+A\_j by column addition does not involve carrying.

### Constraints

* 2 \leq N \leq 10^6
* 0 \leq A\_i \leq 10^6-1
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 A_2 \cdots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4
4 8 12 90
```

### Sample Output 1

```
3
```

The pairs (i,j) that count are (1,3),(1,4),(2,4).

For example, calculation of A\_1+A\_3=4+12 does not involve carrying, so (i,j)=(1,3) counts.
On the other hand, calculation of A\_3+A\_4=12+90 involves carrying, so (i,j)=(3,4) does not count.

---

### Sample Input 2

```
20
313923 246114 271842 371982 284858 10674 532090 593483 185123 364245 665161 241644 604914 645577 410849 387586 732231 952593 249651 36908
```

### Sample Output 2

```
6
```

---

### Sample Input 3

```
5
1 1 1 1 1
```

### Sample Output 3

```
10
```
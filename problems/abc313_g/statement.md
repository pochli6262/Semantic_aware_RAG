Score : 625 points

### Problem Statement

There are N plates numbered 1 through N. Dish i has a\_i stones on it. There is also an empty bag.  
You can perform the following two kinds of operations any number of times (possibly zero) in any order.

* Remove one stone from each plate with one or more stones. Put the removed stones into the bag.
* Take N stones out of the bag, and put one stone to each plate. This operation can be performed only when the bag has N or more stones.

Let b\_i be the number of stones on plate i after you finished the operations. Print the number, modulo 998244353, of sequences of integers (b\_1, b\_2, \dots, b\_N) of length N that can result from the operations.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 0 \leq a\_i \leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N
a_1 a_2 \dots a_N
```

### Output

Print the number, modulo 998244353, of possible sequences (b\_1, b\_2, \dots, b\_N).

---

### Sample Input 1

```
3
3 1 3
```

### Sample Output 1

```
7
```

For example, b becomes (2, 1, 2) by the following procedure.

* Perform the first operation. b becomes (2, 0, 2).
* Perform the first operation. b becomes (1, 0, 1).
* Perform the second operation. b becomes (2, 1, 2).

The following seven sequences can be the resulting b.

* (0, 0, 0)
* (1, 0, 1)
* (1, 1, 1)
* (2, 0, 2)
* (2, 1, 2)
* (2, 2, 2)
* (3, 1, 3)

---

### Sample Input 2

```
1
0
```

### Sample Output 2

```
1
```

There are one sequence, (0), that can be the resulting b.

---

### Sample Input 3

```
5
1 3 5 7 9
```

### Sample Output 3

```
36
```

---

### Sample Input 4

```
10
766294629 440423913 59187619 725560240 585990756 965580535 623321125 550925213 122410708 549392044
```

### Sample Output 4

```
666174028
```
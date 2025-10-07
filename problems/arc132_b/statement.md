Score : 400 points

### Problem Statement

Given is a permutation p\_1,\dots,p\_n of 1,\dots,n.
On this permutation, you can do the operations below any number of times in any order.

* Reverse the entire permutation. That is, rearrange p\_1,p\_2,\dots,p\_n to p\_n,p\_{n-1},\dots,p\_1.
* Move the term at the beginning to the end. That is, rearrange p\_1,p\_2,\dots,p\_n to p\_2,\dots, p\_n, p\_1.

Find the minimum number of operations needed to sort the permutation in ascending order.
In the given input, it is guaranteed that these operations can sort the permutation in ascending order.

### Constraints

* 2 \leq n \leq 10^5
* p\_1,\dots,p\_n is a permutation of 1,\dots,n.
* The operations in Problem Statement can sort p\_1,\dots,p\_n in ascending order.

---

### Input

Input is given from Standard Input in the following format:

```
n
p_1 \dots p_n
```

### Output

Print the minimum number of operations needed to sort the permutation in ascending order.

---

### Sample Input 1

```
3
1 3 2
```

### Sample Output 1

```
2
```

You can sort it in ascending order in two operations as follows.

1. Move the term at the beginning to the end: now you have 3, 2, 1.
2. Reverse the whole permutation: now you have 1, 2, 3.

You cannot sort it in less than two operations, so the answer is 2.

---

### Sample Input 2

```
2
2 1
```

### Sample Output 2

```
1
```

Doing either operation once will sort it in ascending order.

You cannot sort it in less than one operation, so the answer is 1.

---

### Sample Input 3

```
10
2 3 4 5 6 7 8 9 10 1
```

### Sample Output 3

```
3
```

You can sort it in ascending order in three operations as follows.

1. Reverse the whole permutation: now you have 1,10,9,8,7,6,5,4,3,2.
2. Move the term at the beginning to the end: now you have 10,9,8,7,6,5,4,3,2,1.
3. Reverse the whole permutation: now you have 1,2,3,4,5,6,7,8,9,10.

You cannot sort it in less than three operations, so the answer is 3.

---

### Sample Input 4

```
12
1 2 3 4 5 6 7 8 9 10 11 12
```

### Sample Output 4

```
0
```

No operation is needed.
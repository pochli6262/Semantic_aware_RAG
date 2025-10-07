Score : 600 points

### Problem Statement

You are given a sequence A=(A\_1,A\_2,\dots,A\_N) of length N consisting of positive integers, where the elements of A are distinct.

You will choose a positive integer M between 3 and 10^9 (inclusive) to perform the following operation once:

* For each integer i such that 1 \le i \le N, replace A\_i with A\_i \bmod M.

Can you choose an M so that A satisfies the following condition after the operation? If you can, find such an M.

* There exists an integer x such that x is the majority in A.

Here, an integer x is said to be the majority in A if the number of integers i such that A\_i = x is greater than the number of integers i such that A\_i \neq x.

### Constraints

* 3 \le N \le 5000
* 1 \le A\_i \le 10^9
* The elements of A are distinct.
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

If there exists an M that satisfies the condition, print such an M. Otherwise, print -1.

---

### Sample Input 1

```
5
3 17 8 14 10
```

### Sample Output 1

```
7
```

If you let M=7 to perform the operation, you will have A=(3,3,1,0,3), where 3 is the majority in A, so M=7 satisfies the condition.

---

### Sample Input 2

```
10
822848257 553915718 220834133 692082894 567771297 176423255 25919724 849988238 85134228 235637759
```

### Sample Output 2

```
37
```

---

### Sample Input 3

```
10
1 2 3 4 5 6 7 8 9 10
```

### Sample Output 3

```
-1
```
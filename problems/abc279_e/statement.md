Score : 500 points

### Problem Statement

You are given a sequence of length M consisting of integers between 1 and N-1, inclusive: A=(A\_1,A\_2,\dots,A\_M).
Answer the following question for i=1, 2, \dots, M.

* There is a sequence B=(B\_1,B\_2,\dots,B\_N). Initially, we have B\_j=j for each j. Let us perform the following operation for k=1, 2, \dots, i-1, i+1, \dots, M in this order (in other words, for integers k between 1 and M except i in ascending order).
  + Swap the values of B\_{A\_k} and B\_{A\_k+1}.
* After all the operations, let S\_i be the value of j such that B\_j=1. Find S\_i.

### Constraints

* 2 \leq N \leq 2\times 10^5
* 1 \leq M \leq 2\times 10^5
* 1 \leq A\_i \leq N-1\ (1\leq i \leq M)
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 A_2 \dots A_M
```

### Output

Print M lines.
The i-th line (1\leq i \leq M) should contain the value S\_i as an integer.

---

### Sample Input 1

```
5 4
1 2 3 2
```

### Sample Output 1

```
1
3
2
4
```

For i = 2, the operations change B as follows.

* Initially, B = (1,2,3,4,5).
* Perform the operation for k=1. That is, swap the values of B\_1 and B\_2, making B = (2,1,3,4,5).
* Perform the operation for k=3. That is, swap the values of B\_3 and B\_4, making B = (2,1,4,3,5).
* Perform the operation for k=4. That is, swap the values of B\_2 and B\_3, making B = (2,4,1,3,5).

After all the operations, we have B\_3=1, so S\_2 = 3.

Similarly, we have the following.

* For i=1: performing the operation for k=2,3,4 in this order makes B=(1,4,3,2,5), so S\_1=1.
* For i=3: performing the operation for k=1,2,4 in this order makes B=(2,1,3,4,5), so S\_3=2.
* For i=4: performing the operation for k=1,2,3 in this order makes B=(2,3,4,1,5), so S\_4=4.

---

### Sample Input 2

```
3 3
2 2 2
```

### Sample Output 2

```
1
1
1
```

---

### Sample Input 3

```
10 10
1 1 1 9 4 4 2 1 3 3
```

### Sample Output 3

```
2
2
2
3
3
3
1
3
4
4
```
Score : 500 points

### Problem Statement

You are given two sequences of N numbers: A=(A\_1,A\_2,\ldots,A\_N) and B=(B\_1,B\_2,\ldots,B\_N).

Takahashi can repeat the following operation any number of times (possibly zero).

> Choose three pairwise distinct integers i, j, and k between 1 and N.  
> Swap the i-th and j-th elements of A, and swap the i-th and k-th elements of B.

If there is a way for Takahashi to repeat the operation to make A and B equal, print `Yes`; otherwise, print `No`.  
Here, A and B are said to be equal when, for every 1\leq i\leq N, the i-th element of A and that of B are equal.

### Constraints

* 3 \leq N \leq 2\times 10^5
* 1\leq A\_i,B\_i\leq N
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
B_1 B_2 \ldots B_N
```

### Output

Print `Yes` if there is a way for Takahashi to repeat the operation to make A and B equal, and print `No` otherwise.

---

### Sample Input 1

```
3
1 2 1
1 1 2
```

### Sample Output 1

```
Yes
```

Performing the operation once with (i,j,k)=(1,2,3) swaps A\_1 and A\_2, and swaps B\_1 and B\_3,  
making both A and B equal to (2,1,1). Thus, you should print `Yes`.

---

### Sample Input 2

```
3
1 2 2
1 1 2
```

### Sample Output 2

```
No
```

There is no way to perform the operation to make A and B equal, so you should print `No`.

---

### Sample Input 3

```
5
1 2 3 2 1
3 2 2 1 1
```

### Sample Output 3

```
Yes
```

---

### Sample Input 4

```
8
1 2 3 4 5 6 7 8
7 8 5 6 4 3 1 2
```

### Sample Output 4

```
No
```
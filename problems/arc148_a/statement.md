Score : 300 points

### Problem Statement

You are given a sequence A = (A\_1, A\_2, ..., A\_N).  
You may perform the following operation exactly once.

* Choose an integer M at least 2. Then, for every integer i (1 \leq i \leq N), replace A\_i with the remainder when A\_i is divided by M.

For instance, if M = 4 is chosen when A = (2, 7, 4), A becomes (2 \bmod 4, 7 \bmod 4, 4 \bmod 4) = (2, 3, 0).

Find the minimum possible number of different elements in A after the operation.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 0 \leq A\_i \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
1 4 8
```

### Sample Output 1

```
2
```

If you choose M = 3, you will have A = (1 \bmod 3, 4 \bmod 3, 8 \bmod 3) = (1, 1, 2), where A contains two different elements.  
The number of different elements in A cannot become 1, so the answer is 2.

---

### Sample Input 2

```
4
5 10 15 20
```

### Sample Output 2

```
1
```

If you choose M = 5, you will have A = (0, 0, 0, 0), which is optimal.

---

### Sample Input 3

```
10
3785 5176 10740 7744 3999 3143 9028 2822 4748 6888
```

### Sample Output 3

```
1
```
Score : 300 points

### Problem Statement

You are given a string S of length N-1 consisting of `<` and `>`.

A sequence x=(x\_1,x\_2,\cdots,x\_N) of length N is called a **good sequence** if and only if it satisfies the following condition:

* For each i (1 \leq i \leq N-1), if the i-th character of S is `<`, then x\_i\lt x\_{i+1}; if it is `>`, then x\_i \gt x\_{i+1}.

Find the minimum possible inversion number of a good sequence.

What is the inversion number of a sequence?

The inversion number of a sequence x=(x\_1,x\_2,\cdots,x\_n) of length n is the number of pairs of integers (i,j) (1 \leq i < j \leq n) such that x\_i>x\_j.

### Constraints

* 2 \leq N \leq 250000
* S is a string of length N-1 consisting of `<` and `>`.
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
S
```

### Output

Print the answer.

---

### Sample Input 1

```
4
<><
```

### Sample Output 1

```
1
```

x=(1,2,1,2) is a good sequence, and its inversion number is 1.
There is no good sequence whose inversion number is 0, so the answer is 1.

---

### Sample Input 2

```
2
<
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
10
>>>>>>>>>
```

### Sample Output 3

```
45
```

---

### Sample Input 4

```
30
<<><>>><><>><><><<>><<<><><<>
```

### Sample Output 4

```
19
```
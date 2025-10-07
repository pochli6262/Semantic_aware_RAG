Score : 300 points

### Problem Statement

> Planning to place many PCs in his room, Takahashi has decided to write a code that finds how many PCs he can place in his room.

You are given H strings S\_1,S\_2,\ldots,S\_H, each of length W, consisting of `.` and `T`.

Takahashi may perform the following operation any number of times (possibly zero):

* Choose integers satisfying 1\leq i \leq H and 1 \leq j \leq W-1 such that the j-th and (j+1)-th characters of S\_i are both `T`. Replace the j-th character of S\_i with `P`, and (j+1)-th with `C`.

He tries to maximize the number of times he performs the operation. Find possible resulting S\_1,S\_2,\ldots,S\_H.

### Constraints

* 1\leq H \leq 100
* 2\leq W \leq 100
* H and W are integers.
* S\_i is a string of length W consisting of `.` and `T`.

---

### Input

The input is given from Standard Input in the following format:

```
H W 
S_1
S_2
\vdots
S_H
```

### Output

Print a sequence of strings, S\_1,S\_2,\ldots,S\_H, separated by newlines, possibly resulting from maximizing the number of times he performs the operation.

If multiple solutions exist, print any of them.

---

### Sample Input 1

```
2 3
TTT
T.T
```

### Sample Output 1

```
PCT
T.T
```

He can perform the operation at most once.

For example, an operation with (i,j)=(1,1) makes S\_1 `PCT`.

---

### Sample Input 2

```
3 5
TTT..
.TTT.
TTTTT
```

### Sample Output 2

```
PCT..
.PCT.
PCTPC
```
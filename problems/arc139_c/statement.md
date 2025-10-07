Score : 700 points

### Problem Statement

You are given positive integers N and M.

Let us call a sequence of pairs of integers ((X\_1,Y\_1),(X\_2,Y\_2),\dots,(X\_K,Y\_K)) **wonderful** when it satisfies the following.

* 1 \le X\_i \le N
* 1 \le Y\_i \le M
* X\_i+3Y\_i \neq X\_j+3Y\_j and 3X\_i+Y\_i \neq 3X\_j+Y\_j, if i \neq j.

Make a wonderful sequence of pairs of integers whose length, K, is the maximum possible.

### Constraints

* 1 \le N,M \le 10^5
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
```

### Output

Print your answer in the following format:

```
K
X_1 Y_1
X_2 Y_2
\vdots
X_K Y_K
```

Here, K should be the maximum possible length of a wonderful sequence of pairs of integers, and ((X\_1,Y\_1),(X\_2,Y\_2),\dots,(X\_K,Y\_K)) should be a wonderful sequence of pairs of integers.
If multiple solutions exist, printing any of them is accepted.

---

### Sample Input 1

```
3 4
```

### Sample Output 1

```
10
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
3 4
```

For N=3, M=4, there is no wonderful sequence of pairs of integers whose length is 11 or longer, and the above sequence of pairs of integers is wonderful, so this output is valid.
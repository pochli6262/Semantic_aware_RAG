Score : 500 points

### Problem Statement

You are given a string S of length N consisting of `o` and `x`, and integers M and K.  
S is guaranteed to contain at least one `x`.

Let T be the string of length NM obtained by concatenating M copies of S.
Consider replacing exactly K `x`'s in T with `o`.  
Your objective is to have as long a contiguous substring consisting of `o` as possible in the resulting T.  
Find the maximum length of a contiguous substring consisting of `o` that you can obtain.

### Constraints

* N, M, and K are integers.
* 1 \le N \le 3 \times 10^5
* 1 \le M \le 10^9
* 1 \le K \le x, where x is the number of `x`'s in the string T.
* S is a string of length N consisting of `o` and `x`.
* S has at least one `x`.

---

### Input

The input is given from Standard Input in the following format:

```
N M K
S
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
10 1 2
ooxxooooox
```

### Sample Output 1

```
9
```

S= `ooxxooooox` and T= `ooxxooooox`.  
Replacing `x` at the third and fourth characters with `o` makes T= `ooooooooox`.  
Now we have a length-9 contiguous substring consisting of `o`, which is the longest possible.

---

### Sample Input 2

```
5 3 4
oxxox
```

### Sample Output 2

```
8
```

S= `oxxox` and T= `oxxoxoxxoxoxxox`.  
Replacing `x` at the 5,7,8 and 10-th characters with `o` makes T= `oxxooooooooxxox`.  
Now we have a length-8 contiguous substring consisting of `o`, which is the longest possible.

---

### Sample Input 3

```
30 1000000000 9982443530
oxoxooxoxoxooxoxooxxxoxxxooxox
```

### Sample Output 3

```
19964887064
```
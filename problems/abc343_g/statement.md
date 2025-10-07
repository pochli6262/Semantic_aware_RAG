Score: 600 points

### Problem Statement

You are given N strings S\_1, S\_2, \ldots, S\_N.

Find the minimum length of a string that contains all these strings as substrings.

Here, a string S contains a string T as a substring if T can be obtained by deleting zero or more characters from the beginning and zero or more characters from the end of S.

### Constraints

* N is an integer.
* 1 \leq N \leq 20
* S\_i is a string consisting of lowercase English letters whose length is at least 1.
* The total length of S\_1, S\_2, \dots, S\_N is at most 2\times 10^5.

---

### Input

The input is given from Standard Input in the following format:

```
N
S_1
S_2
\vdots
S_N
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
3
snuke
kensho
uk
```

### Sample Output 1

```
9
```

The string `snukensho` of length 9 contains all of S\_1, S\_2, and S\_3 as substrings.

Specifically, the first to fifth characters of `snukensho` correspond to S\_1, the fourth to ninth correspond to S\_2, and the third to fourth correspond to S\_3.

No shorter string contains all of S\_1, S\_2, and S\_3 as substrings.
Thus, the answer is 9.

---

### Sample Input 2

```
3
abc
abc
arc
```

### Sample Output 2

```
6
```

---

### Sample Input 3

```
6
cmcmrcc
rmrrrmr
mrccm
mmcr
rmmrmrcc
ccmcrcmcm
```

### Sample Output 3

```
27
```
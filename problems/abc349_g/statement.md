Score: 625 points

### Problem Statement

A sequence of positive integers T=(T\_1,T\_2,\dots,T\_M) of length M is a **palindrome** if and only if T\_i=T\_{M-i+1} for each i=1,2,\dots,M.

You are given a sequence of non-negative integers A = (A\_1,A\_2,\dots,A\_N) of length N. Determine if there is a sequence of positive integers S=(S\_1,S\_2,\dots,S\_N) of length N that satisfies the following condition, and if it exists, find the lexicographically smallest such sequence.

* For each i=1,2,\dots,N, both of the following hold:
  + The sequence (S\_{i-A\_i},S\_{i-A\_i+1},\dots,S\_{i+A\_i}) is a palindrome.
  + If 2 \leq i-A\_i and i+A\_i \leq N-1, the sequence (S\_{i-A\_i-1},S\_{i-A\_i},\dots,S\_{i+A\_i+1}) is not a palindrome.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 0 \leq A\_i \leq \min\{i-1,N-i\}
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

If there is no sequence S that satisfies the condition, print `No`.

If there is a sequence S that satisfies the condition, let S' be the lexicographically smallest such sequence and print it in the following format:

```
Yes
S'_1 S'_2 \dots S'_N
```

---

### Sample Input 1

```
7
0 0 2 0 2 0 0
```

### Sample Output 1

```
Yes
1 1 2 1 1 1 2
```

S = (1,1,2,1,1,1,2) satisfies the condition:

* i=1: (A\_1)=(1) is a palindrome.
* i=2: (A\_2)=(1) is a palindrome, but (A\_1,A\_2,A\_3)=(1,1,2) is not.
* i=3: (A\_1,A\_2,\dots,A\_5)=(1,1,2,1,1) is a palindrome.
* i=4: (A\_4)=(1) is a palindrome, but (A\_3,A\_4,A\_5)=(2,1,1) is not.
* i=5: (A\_3,A\_4,\dots,A\_7)=(2,1,1,1,2) is a palindrome.
* i=6: (A\_6)=(1) is a palindrome, but (A\_5,A\_6,A\_7)=(1,1,2) is not.
* i=7: (A\_7)=(2) is a palindrome.

There are other sequences like S=(2,2,1,2,2,2,1) that satisfy the condition, but print the lexicographically smallest one, which is (1,1,2,1,1,1,2).

---

### Sample Input 2

```
7
0 1 2 3 2 1 0
```

### Sample Output 2

```
Yes
1 1 1 1 1 1 1
```

---

### Sample Input 3

```
7
0 1 2 0 2 1 0
```

### Sample Output 3

```
No
```
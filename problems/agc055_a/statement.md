Score : 400 points

### Problem Statement

You are given a string S of length 3N, containing exactly N letters `A`, N letters `B`, and N letters `C`.

Let's call a string T consisting of letters `A`, `B`, and `C` **good**, if the following conditions hold:

* The length of T is divisible by 3. Let's denote it by 3K.
* T\_1 = T\_2 = \ldots = T\_K
* T\_{K+1} = T\_{K+2} = \ldots = T\_{2K}
* T\_{2K+1} = T\_{2K+2} = \ldots = T\_{3K}.
* Letters T\_1, T\_{K+1} and T\_{2K+1} are different from each other.

Examples of good strings are `ABC`, `BBAACC`, and `AAACCCBBB`.

Find a way to split S into **at most 6** (not necessarily contiguous) subsequences so that the letters from each subsequence form a good string.

It can be proved that, under the constraints of the problem, it's always possible.

### Constraints

* 1 \le N \le 2\cdot 10^5
* The string S contains N letters `A`, N letters `B`, and N letters `C`.

---

### Input

Input is given from Standard Input in the following format:

```
N
S
```

### Output

Output a string of length 3N, containing only digits from 1 to 6.
For every 1\le i \le 6 which appears in your string, characters of S at positions where you output i have to form a good string.
If there are multiple possible solutions, printing any of them will be considered correct.

---

### Sample Input 1

```
2
ABCCBA
```

### Sample Output 1

```
111222
```

S is split into subsequences `ABC` and `CBA`, and each of them is a good string.

---

### Sample Input 2

```
4
AABCBCAACBCB
```

### Sample Output 2

```
111211241244
```

Positions of 1 form a subsequence `AABBCC`, positions of 2 form a subsequence `CAB`, and positions of 4 form a subsequence `ACB`.
All of these strings are good.
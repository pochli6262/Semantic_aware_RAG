Score : 700 points

### Problem Statement

Let us define the **beauty** of the string as the number of positions where two adjacent characters are the same.
For example, the beauty of `00011` is 3, and the beauty of `10101` is 0.

Let S\_{n,m} be the set of all strings of length n+m formed of n `0`s and m `1`s.

For s\_1,s\_2 \in S\_{n,m}, let us define the **distance** of s\_1 and s\_2, d(s\_1,s\_2), as the minimum number of swaps needed when rearranging the string s\_1 to s\_2 by swaps of two adjacent characters.

Additionally, for s\_1,s\_2,s\_3\in S\_{n,m}, s\_2 is said to be **between** s\_1 and s\_3 when d(s\_1,s\_3)=d(s\_1,s\_2)+d(s\_2,s\_3).

Given s,t\in S\_{n,m}, print the greatest beauty of a string between s and t.

### Constraints

* 2 \le n + m\le 3\times 10^5
* 0 \le n,m
* Each of s and t is a string of length n+m formed of n `0`s and m `1`s.

---

### Input

Input is given from Standard Input in the following format:

```
n m
s
t
```

### Output

Print the greatest beauty of a string between s and t.

---

### Sample Input 1

```
2 3
10110
01101
```

### Sample Output 1

```
2
```

Between `10110` and `01101`, whose distance is 2, we have the following strings: `10110`, `01110`, `01101`, `10101`.
Their beauties are 1, 2, 1, 0, respectively, so the answer is 2.

---

### Sample Input 2

```
4 2
000011
110000
```

### Sample Output 2

```
4
```

Between `000011` and `110000`, whose distance is 8, the strings with the greatest beauty are `000011` and `110000`, so the answer is 4.

---

### Sample Input 3

```
12 26
01110111101110111101001101111010110110
10011110111011011001111011111101001110
```

### Sample Output 3

```
22
```
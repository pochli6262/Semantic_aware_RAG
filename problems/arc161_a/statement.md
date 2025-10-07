Score : 300 points

### Problem Statement

Let N be a positive **odd** number.
A sequence of integers of length N, S = (S\_1, S\_2, \dots, S\_N), is said to be **M-type** if "for each even number i = 2, 4, \dots, N - 1, it holds that S\_{i-1} < S\_i and S\_i > S\_{i+1}".

You are given a sequence of positive integers of length N, A = (A\_1, A\_2, \dots, A\_N).
Determine if it is possible to rearrange A to be M-type.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* N is an **odd** number.
* 1 \leq A\_i \leq 10^9 \ \ (1 \leq i \leq N)

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 \ A_2 \ \dots \ A_N
```

### Output

If it is possible to rearrange the given integer sequence A to be M-type, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
5
1 2 3 4 5
```

### Sample Output 1

```
Yes
```

The given sequence is A = (1, 2, 3, 4, 5).
After rearranging it, for example, to B = (4, 5, 1, 3, 2),

* for i = 2, it holds that B\_1 = 4 < 5 = B\_2 and B\_2 = 5 > 1 = B\_3;
* for i = 4, it holds that B\_3 = 1 < 3 = B\_4 and B\_4 = 3 > 2 = B\_5.

Therefore, this sequence B is M-type, and the answer is `Yes`.

---

### Sample Input 2

```
5
1 6 1 6 1
```

### Sample Output 2

```
Yes
```

The given sequence A itself is M-type.

---

### Sample Input 3

```
5
1 6 6 6 1
```

### Sample Output 3

```
No
```

It is impossible to rearrange it to be M-type.
Score : 300 points

### Problem Statement

Given are integers N, L, and R.
Count the number of integers x that satisfy both of the following conditions.

* L \leq x \leq R
* (x \oplus N) < N (Here, \oplus denotes the bitwise \mathrm{XOR}.）

What is the bitwise \mathrm{XOR}?

The bitwise \mathrm{XOR} of integers A and B, A\oplus B, is defined as follows:

* When A\oplus B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if exactly one of A and B is 1, and 0 otherwise.

For example, we have 3\oplus 5 = 6 (in base two: 011\oplus 101 = 110).

### Constraints

* 1 \leq N \leq 10^{18}
* 1 \leq L \leq R \leq 10^{18}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N L R
```

### Output

Print the answer.

---

### Sample Input 1

```
2 1 2
```

### Sample Output 1

```
1
```

For x=1, L \leq x \leq R is satisfied, but (x \oplus N) < N is not.
For x=2, both conditions are satisfied.
There is no other x that satisfies the conditions.

---

### Sample Input 2

```
10 2 19
```

### Sample Output 2

```
10
```

---

### Sample Input 3

```
1000000000000000000 1 1000000000000000000
```

### Sample Output 3

```
847078495393153025
```
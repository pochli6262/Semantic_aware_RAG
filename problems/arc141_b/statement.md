Score : 500 points

### Problem Statement

You are given positive integers N and M.

Find the number of sequences A=(A\_1,\ A\_2,\ \dots,\ A\_N) of N positive integers that satisfy the following conditions, modulo 998244353.

* 1 \leq A\_1 < A\_2 < \dots < A\_N \leq M.
* B\_1 < B\_2 < \dots < B\_N, where B\_i = A\_1 \oplus A\_2 \oplus \dots \oplus A\_i.

Here, \oplus denotes bitwise \mathrm{XOR}.

What is bitwise \mathrm{XOR}?

The bitwise \mathrm{XOR} of non-negative integers A and B, A \oplus B, is defined as follows:

* When A \oplus B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if exactly one of A and B is 1, and 0 otherwise.

For example, we have 3 \oplus 5 = 6 (in base two: 011 \oplus 101 = 110).  
Generally, the bitwise \mathrm{XOR} of k non-negative integers p\_1, p\_2, p\_3, \dots, p\_k is defined as (\dots ((p\_1 \oplus p\_2) \oplus p\_3) \oplus \dots \oplus p\_k). We can prove that this value does not depend on the order of p\_1, p\_2, p\_3, \dots, p\_k.

### Constraints

* 1 \leq N \leq M < 2^{60}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
```

### Output

Print the answer.

---

### Sample Input 1

```
2 4
```

### Sample Output 1

```
5
```

For example, (A\_1,\ A\_2)=(1,\ 3) counts, since A\_1 < A\_2 and B\_1 < B\_2 where B\_1=A\_1=1,\ B\_2=A\_1\oplus A\_2=2.

The other pairs that count are (A\_1,\ A\_2)=(1,\ 2),\ (1,\ 4),\ (2,\ 4),\ (3,\ 4).

---

### Sample Input 2

```
4 4
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
10 123456789
```

### Sample Output 3

```
205695670
```
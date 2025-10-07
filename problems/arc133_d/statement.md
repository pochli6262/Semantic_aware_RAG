Score : 700 points

### Problem Statement

Given are integers L, R, and V.
Find the number of pairs of integers (l,r) that satisfy both of the conditions below, modulo 998244353.

* L \leq l \leq r \leq R
* l \oplus (l+1) \oplus \cdots \oplus r=V

Here, \oplus denotes the bitwise \mathrm{XOR} operation.

What is bitwise \mathrm{XOR}?

The bitwise \mathrm{XOR} of non-negative integers A and B, A \oplus B, is defined as follows:

* When A \oplus B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if exactly one of A and B is 1, and 0 otherwise.

For example, we have 3 \oplus 5 = 6 (in base two: 011 \oplus 101 = 110).  
Generally, the bitwise \mathrm{XOR} of k integers p\_1, p\_2, p\_3, \dots, p\_k is defined as (\dots ((p\_1 \oplus p\_2) \oplus p\_3) \oplus \dots \oplus p\_k). We can prove that this value does not depend on the order of p\_1, p\_2, p\_3, \dots p\_k.

### Constraints

* 1 \leq L \leq R \leq 10^{18}
* 0 \leq V \leq 10^{18}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
L R V
```

### Output

Print the answer.

---

### Sample Input 1

```
1 3 3
```

### Sample Output 1

```
2
```

The two pairs satisfying the conditions are (l,r)=(1,2) and (l,r)=(3,3).

---

### Sample Input 2

```
10 20 0
```

### Sample Output 2

```
6
```

---

### Sample Input 3

```
1 1 1
```

### Sample Output 3

```
1
```

---

### Sample Input 4

```
12345 56789 34567
```

### Sample Output 4

```
16950
```
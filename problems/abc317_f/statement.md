Score : 500 points

### Problem Statement

You are given integers N,A\_1,A\_2,A\_3. Find the number, modulo 998244353, of triples of positive integers (X\_1,X\_2,X\_3) that satisfy all of the following three conditions.

* 1\leq X\_i \leq N for every i.
* X\_i is a multiple of A\_i for every i.
* (X\_1 \oplus X\_2) \oplus X\_3 = 0, where \oplus denotes bitwise xor.

What is bitwise xor?
The bitwise xor of non-negative integers A and B, A \oplus B, is defined as follows.

* When A \oplus B is written in binary, the 2^ks place (k \geq 0) is 1 if exactly one of the 2^ks places of A and B is 1, and 0 otherwise.

For instance, 3 \oplus 5 = 6 (in binary: 011 \oplus 101 = 110).

### Constraints

* 1 \leq N \leq 10^{18}
* 1 \leq A\_i \leq 10
* All input values are integers.

---

### Input

The Input is given from Standard Input in the following format:

```
N A_1 A_2 A_3
```

### Output

Print the answer.

---

### Sample Input 1

```
13 2 3 5
```

### Sample Output 1

```
4
```

Four triples (X\_1,X\_2,X\_3) satisfy the conditions: (6,3,5),(6,12,10),(12,6,10),(12,9,5).

---

### Sample Input 2

```
1000000000000000000 1 1 1
```

### Sample Output 2

```
426724011
```

---

### Sample Input 3

```
31415926535897932 3 8 4
```

### Sample Output 3

```
759934997
```
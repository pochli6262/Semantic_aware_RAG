Score : 700 points

### Problem Statement

You are given an integer sequence of length N: A=(A\_1,A\_2,\cdots,A\_N), and an integer M.

For each k=1,2,\cdots,M, find the value of A\_N after doing the operation below k times.

* For every i (1 \leq i \leq N), simultaneously, replace the value of A\_i with A\_1 \oplus A\_2 \oplus \cdots \oplus A\_i.

Here, \oplus denotes bitwise \mathrm{XOR}.

What is bitwise \mathrm{XOR}?

The bitwise \mathrm{XOR} of non-negative integers A and B, A \oplus B, is defined as follows:

* When A \oplus B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if exactly one of A and B is 1, and 0 otherwise.

For example, we have 3 \oplus 5 = 6 (in base two: 011 \oplus 101 = 110).  
Generally, the bitwise \mathrm{XOR} of k integers p\_1, p\_2, p\_3, \dots, p\_k is defined as (\dots ((p\_1 \oplus p\_2) \oplus p\_3) \oplus \dots \oplus p\_k). We can prove that this value does not depend on the order of p\_1, p\_2, p\_3, \dots p\_k.

### Constraints

* 1 \leq N \leq 10^6
* 1 \leq M \leq 10^6
* 0 \leq A\_i < 2^{30}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
A_1 A_2 \cdots A_N
```

### Output

Print the answers for respective values of k, separated by spaces.

---

### Sample Input 1

```
3 2
2 1 3
```

### Sample Output 1

```
0 1
```

Each operation changes A as follows.

* Initially: A=(2,1,3).
* After the first operation: A=(2,3,0).
* After the second operation: A=(2,1,1).

---

### Sample Input 2

```
10 12
721939838 337089195 171851101 1069204754 348295925 77134863 839878205 89360649 838712948 918594427
```

### Sample Output 2

```
716176219 480674244 678890528 642764255 259091950 663009497 942498522 584528336 364872846 145822575 392655861 844652404
```
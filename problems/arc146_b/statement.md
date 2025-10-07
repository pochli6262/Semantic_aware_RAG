Score : 500 points

### Problem Statement

You are given a sequence of N non-negative integers: A=(A\_1,A\_2,\dots,A\_N). You may perform the following operation at most M times (possibly zero):

* choose an integer i such that 1 \le i \le N and add 1 to A\_i.

Then, you will choose K of the elements of A.

Find the maximum possible value of the bitwise \mathrm{AND} of the elements you choose.

What is bitwise {\rm AND}?

The bitwise {\rm AND} of non-negative integers A and B, A\ \mathrm{AND}\ B, is defined as follows:

* When A\ {\rm AND}\ B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if both of the digits in that place of A and B are 1, and 0 otherwise.

For example, 3\ {\rm AND}\ 5 = 1. (In base two, 011\ {\rm AND}\ 101 = 001.)  
Generally, the bitwise {\rm AND} of k non-negative integers p\_1, p\_2, p\_3, \dots, p\_k is defined as (\dots ((p\_1\ \mathrm{AND}\ p\_2)\ \mathrm{AND}\ p\_3)\ \mathrm{AND}\ \dots\ \mathrm{AND}\ p\_k). We can prove that this value does not depend on the order of p\_1, p\_2, p\_3, \dots, p\_k.

​

### Constraints

* 1 \le K \le N \le 2 \times 10^5
* 0 \le M < 2^{30}
* 0 \le A\_i < 2^{30}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M K
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 8 2
1 2 4 8
```

### Sample Output 1

```
10
```

If you do the following, the bitwise \mathrm{AND} of the elements you choose will be 10.

* Perform the operation on A\_3 six times. Now, A\_3 = 10.
* Perform the operation on A\_4 twice. Now, A\_4 = 10.
* Choose A\_3 and A\_4, whose bitwise \mathrm{AND} is 10.

There is no way to choose two elements whose bitwise \mathrm{AND} is greater than 10, so the answer is 10.

---

### Sample Input 2

```
5 345 3
111 192 421 390 229
```

### Sample Output 2

```
461
```
Score : 500 points

### Problem Statement

Let us call a positive integer n that satisfies the following condition an **arithmetic number**.

* Let d\_i be the i-th digit of n from the top (when n is written in base 10 without unnecessary leading zeros.) Then, (d\_2-d\_1)=(d\_3-d\_2)=\dots=(d\_k-d\_{k-1}) holds, where k is the number of digits in n.
  + This condition can be rephrased into the sequence (d\_1,d\_2,\dots,d\_k) being arithmetic.
  + If n is a 1-digit integer, it is assumed to be an arithmetic number.

For example, 234,369,86420,17,95,8,11,777 are arithmetic numbers, while 751,919,2022,246810,2356 are not.

Find the smallest arithmetic number not less than X.

### Constraints

* X is an integer between 1 and 10^{17} (inclusive).

---

### Input

Input is given from Standard Input in the following format:

```
X
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
152
```

### Sample Output 1

```
159
```

The smallest arithmetic number not less than 152 is 159.

---

### Sample Input 2

```
88
```

### Sample Output 2

```
88
```

X itself may be an arithmetic number.

---

### Sample Input 3

```
8989898989
```

### Sample Output 3

```
9876543210
```
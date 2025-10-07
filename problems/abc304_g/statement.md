Score : 625 points

### Problem Statement

You are given a sequence of length 2N: A = (A\_1, A\_2, \ldots, A\_{2N}).

Find the maximum value that can be obtained as the median of the length-N sequence (A\_1 \oplus A\_2, A\_3 \oplus A\_4, \ldots, A\_{2N-1} \oplus A\_{2N}) by rearranging the elements of the sequence A.

Here, \oplus represents bitwise exclusive OR.

What is bitwise exclusive OR? The bitwise exclusive OR of non-negative integers A and B, denoted as A \oplus B, is defined as follows:

* The number at the 2^k position (k \geq 0) in the binary representation of A \oplus B is 1 if and only if exactly one of the numbers at the 2^k position in the binary representation of A and B is 1, and it is 0 otherwise.

For example, 3 \oplus 5 = 6 (in binary notation: 011 \oplus 101 = 110). 

Also, for a sequence B of length L, the median of B is the value at the \lfloor \frac{L}{2} \rfloor + 1-th position of the sequence B' obtained by sorting B in ascending order.

### Constraints

* 1 \leq N \leq 10^5
* 0 \leq A\_i < 2^{30}
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_{2N}
```

### Output

Print the answer.

---

### Sample Input 1

```
4
4 0 0 11 2 7 9 5
```

### Sample Output 1

```
14
```

By rearranging A as (5, 0, 9, 7, 11, 4, 0, 2), we get (A\_1 \oplus A\_2, A\_3 \oplus A\_4, A\_5 \oplus A\_6, A\_7 \oplus A\_8) = (5, 14, 15, 2), and the median of this sequence is 14.  
It is impossible to rearrange A so that the median of (A\_1 \oplus A\_2, A\_3 \oplus A\_4, A\_5 \oplus A\_6, A\_7 \oplus A\_8) is 15 or greater, so we print 14.

---

### Sample Input 2

```
1
998244353 1000000007
```

### Sample Output 2

```
1755654
```

---

### Sample Input 3

```
5
1 2 4 8 16 32 64 128 256 512
```

### Sample Output 3

```
192
```
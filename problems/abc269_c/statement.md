Score : 300 points

### Problem Statement

You are given a non-negative integer N. Print all non-negative integers x that satisfy the following condition in ascending order.

* The set of the digit positions containing 1 in the binary representation of x is a subset of the set of the digit positions containing 1 in the binary representation of N.
  + That is, the following holds for every non-negative integer k: if the digit in the "2^ks" place of x is 1, the digit in the 2^ks place of N is 1.

### Constraints

* N is an integer.
* 0 \le N < 2^{60}
* In the binary representation of N, at most 15 digit positions contain 1.

---

### Input

The input is given from Standard Input in the following format:

```
N
```

### Output

Print the answer as decimal integers in ascending order, each in its own line.

---

### Sample Input 1

```
11
```

### Sample Output 1

```
0
1
2
3
8
9
10
11
```

The binary representation of N = 11\_{(10)} is 1011\_{(2)}.  
The non-negative integers x that satisfy the condition are:

* 0000\_{(2)}=0\_{(10)}
* 0001\_{(2)}=1\_{(10)}
* 0010\_{(2)}=2\_{(10)}
* 0011\_{(2)}=3\_{(10)}
* 1000\_{(2)}=8\_{(10)}
* 1001\_{(2)}=9\_{(10)}
* 1010\_{(2)}=10\_{(10)}
* 1011\_{(2)}=11\_{(10)}

---

### Sample Input 2

```
0
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
576461302059761664
```

### Sample Output 3

```
0
524288
549755813888
549756338176
576460752303423488
576460752303947776
576461302059237376
576461302059761664
```

The input may not fit into a 32-bit signed integer.
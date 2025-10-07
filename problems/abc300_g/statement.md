Score : 600 points

### Problem Statement

A positive integer is called a k-smooth number if none of its prime factors exceeds k.  
Given an integer N and a prime P not exceeding 100, find the number of P-smooth numbers not exceeding N.

### Constraints

* N is an integer such that 1 \le N \le 10^{16}.
* P is a prime such that 2 \le P \le 100.

---

### Input

The input is given from Standard Input in the following format:

```
N P
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
36 3
```

### Sample Output 1

```
14
```

The 3-smooth numbers not exceeding 36 are the following 14 integers: 1,2,3,4,6,8,9,12,16,18,24,27,32,36.  
Note that 1 is a k-smooth number for all primes k.

---

### Sample Input 2

```
10000000000000000 97
```

### Sample Output 2

```
2345134674
```
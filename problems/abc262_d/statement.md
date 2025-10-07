Score : 400 points

### Problem Statement

You are given a sequence of positive integers A=(a\_1,\ldots,a\_N) of length N.  
There are (2^N-1) ways to choose one or more terms of A. How many of them have an integer-valued average? Find the count modulo 998244353.

### Constraints

* 1 \leq N \leq 100
* 1 \leq a\_i \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
a_1 \ldots a_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
2 6 2
```

### Sample Output 1

```
6
```

For each way to choose terms of A, the average is obtained as follows:

* If just a\_1 is chosen, the average is \frac{a\_1}{1}=\frac{2}{1} = 2, which is an integer.
* If just a\_2 is chosen, the average is \frac{a\_2}{1}=\frac{6}{1} = 6, which is an integer.
* If just a\_3 is chosen, the average is \frac{a\_3}{1}=\frac{2}{1} = 2, which is an integer.
* If a\_1 and a\_2 are chosen, the average is \frac{a\_1+a\_2}{2}=\frac{2+6}{2} = 4, which is an integer.
* If a\_1 and a\_3 are chosen, the average is \frac{a\_1+a\_3}{2}=\frac{2+2}{2} = 2, which is an integer.
* If a\_2 and a\_3 are chosen, the average is \frac{a\_2+a\_3}{2}=\frac{6+2}{2} = 4, which is an integer.
* If a\_1, a\_2, and a\_3 are chosen, the average is \frac{a\_1+a\_2+a\_3}{3}=\frac{2+6+2}{3} = \frac{10}{3}, which is not an integer.

Therefore, 6 ways satisfy the condition.

---

### Sample Input 2

```
5
5 5 5 5 5
```

### Sample Output 2

```
31
```

Regardless of the choice of one or more terms of A, the average equals 5.
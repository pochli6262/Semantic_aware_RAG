Score : 500 points

### Problem Statement

Find \displaystyle \sum\_{k=0}^{10^{100}} \left \lfloor \frac{X}{10^k} \right \rfloor.

### Notes

\lfloor A \rfloor denotes the value of A truncated to an integer.

### Constraints

* X is an integer.
* 1 \le X < 10^{500000}

---

### Input

Input is given from Standard Input in the following format:

```
X
```

### Output

Print the answer as an integer.  
Here, the answer must be precisely printed as an integer, even if it is large. It is not allowed to use exponential notation, such as `2.33e+21`, or print unnecessary leading zeros, as in `0523`.

---

### Sample Input 1

```
1225
```

### Sample Output 1

```
1360
```

The value we seek is 1225+122+12+1+0+0+\dots+0=1360.

---

### Sample Input 2

```
99999
```

### Sample Output 2

```
111105
```

Beware of carries.

---

### Sample Input 3

```
314159265358979323846264338327950288419716939937510
```

### Sample Output 3

```
349065850398865915384738153697722542688574377708317
```

The values in input and output can both be enormous.
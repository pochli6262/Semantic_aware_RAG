Score : 400 points

### Problem Statement

There is a sequence A=(A\_0,\ldots,A\_{N-1}) of length N.  
Determine if there exists a tuple of integers (x,y,z,w) that satisfies all of the following conditions:

* 0 \leq x < y < z < w \leq N
* A\_x + A\_{x+1} + \ldots + A\_{y-1} = P
* A\_y + A\_{y+1} + \ldots + A\_{z-1} = Q
* A\_z + A\_{z+1} + \ldots + A\_{w-1} = R

### Constraints

* 3 \leq N \leq 2\times 10^5
* 1 \leq A\_i \leq 10^9
* 1 \leq P,Q,R \leq 10^{15}
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N P Q R
A_0 A_1 \ldots A_{N-1}
```

### Output

If there exists a tuple that satisfies the conditions, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
10 5 7 5
1 3 2 2 2 3 1 4 3 2
```

### Sample Output 1

```
Yes
```

(x,y,z,w)=(1,3,6,8) satisfies the conditions.

---

### Sample Input 2

```
9 100 101 100
31 41 59 26 53 58 97 93 23
```

### Sample Output 2

```
No
```

---

### Sample Input 3

```
7 1 1 1
1 1 1 1 1 1 1
```

### Sample Output 3

```
Yes
```
Score : 600 points

### Problem Statement

Takahashi has A apple seedlings, B banana seedlings, and C cherry seedlings. Seedlings of the same kind cannot be distinguished.  
He will plant these seedlings in his N gardens so that all of the following conditions are satisfied.

* At least one seedling must be planted in every garden.
* It is not allowed to plant two or more seedlings of the same kind in the same garden.
* It is not necessary to plant all seedlings he has.

How many ways are there to plant seedlings to satisfy the conditions? Find the count modulo 998244353.  
Two ways are distinguished when there is a garden with different sets of seedlings planted in these two ways.

### Constraints

* 1 \leq N \leq 5 \times 10^6
* 0 \leq A \leq N
* 0 \leq B \leq N
* 0 \leq C \leq N
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N A B C
```

### Output

Print the answer.

---

### Sample Input 1

```
2 2 1 1
```

### Sample Output 1

```
21
```

As illustrated below, there are 21 ways to plant seedlings to satisfy the conditions.  
(The two frames arranged vertically are the gardens. A, B, C stand for apple, banana, cherry, respectively.)

![image](https://img.atcoder.jp/ghi/30cbec3c4cc587889e3c37933da06c3f.png)

---

### Sample Input 2

```
2 0 0 0
```

### Sample Output 2

```
0
```

There may be no way to plant seedlings to satisfy the conditions.

---

### Sample Input 3

```
2 0 2 2
```

### Sample Output 3

```
9
```

---

### Sample Input 4

```
100 12 34 56
```

### Sample Output 4

```
769445780
```

---

### Sample Input 5

```
5000000 2521993 2967363 3802088
```

### Sample Output 5

```
264705492
```
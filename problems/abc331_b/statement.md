Score : 200 points

### Problem Statement

A supermarket sells egg packs.

A pack of 6 eggs costs S yen, a pack of 8 eggs costs M yen, and a pack of 12 eggs costs L yen.

When you can buy any number of each pack, find the minimum amount of money required to purchase at least N eggs.

### Constraints

* 1 \leq N \leq 100
* 1 \leq S,M,L \leq 10^4
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N S M L
```

### Output

Print the answer.

---

### Sample Input 1

```
16 120 150 200
```

### Sample Output 1

```
300
```

It is optimal to buy two 8-egg packs.

---

### Sample Input 2

```
10 100 50 10
```

### Sample Output 2

```
10
```

It is optimal to buy one 12-egg pack.

---

### Sample Input 3

```
99 600 800 1200
```

### Sample Output 3

```
10000
```

It is optimal to buy five 8-egg packs and five 12-egg packs.
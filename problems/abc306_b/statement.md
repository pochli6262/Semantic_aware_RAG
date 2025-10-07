Score : 200 points

### Problem Statement

You are given a sequence A=(A\_0,A\_1,\dots,A\_{63}) of length 64 consisting of 0 and 1.

Find A\_0 2^0 + A\_1 2^1 + \dots + A\_{63} 2^{63}.

### Constraints

* A\_i is 0 or 1.

---

### Input

The input is given from Standard Input in the following format:

```
A_0 A_1 \dots A_{63}
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

### Sample Output 1

```
13
```

A\_0 2^0 + A\_1 2^1 + \dots + A\_{63} 2^{63} = 2^0 + 2^2 + 2^3 = 13.

---

### Sample Input 2

```
1 0 1 0 1 0 0 0 0 1 0 0 1 1 0 1 1 1 1 0 0 0 1 0 0 1 1 1 1 1 1 0 0 0 0 1 0 1 0 1 0 1 1 1 1 0 0 1 1 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0
```

### Sample Output 2

```
766067858140017173
```
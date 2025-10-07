Score : 200 points

### Problem Statement

A regular pentagon P is shown in the figure below.

![](https://img.atcoder.jp/abc333/2d0c9295b03ff6d808c1ee9125045fc8.png)

Determine whether the length of the line segment connecting points S\_1 and S\_2 of P equals the length of the line segment connecting points T\_1 and T\_2.

### Constraints

* Each of S\_1, S\_2, T\_1, and T\_2 is one of the characters `A`, `B`, `C`, `D`, and `E`.
* S\_1 \neq S\_2
* T\_1 \neq T\_2

---

### Input

The input is given from Standard Input in the following format:

```
S_1S_2
T_1T_2
```

### Output

If the length of the line segment connecting points S\_1 and S\_2 of P equals the length of the line segment connecting points T\_1 and T\_2, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
AC
EC
```

### Sample Output 1

```
Yes
```

The length of the line segment connecting point `A` and point `C` of P equals the length of the line segment connecting point `E` and point `C`.

---

### Sample Input 2

```
DA
EA
```

### Sample Output 2

```
No
```

The length of the line segment connecting point `D` and point `A` of P does not equal the length of the line segment connecting point `E` and point `A`.

---

### Sample Input 3

```
BD
BD
```

### Sample Output 3

```
Yes
```
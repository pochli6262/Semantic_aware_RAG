Score : 600 points

### Problem Statement

You are given integers R, G, B, and K. How many strings S consisting of `R`, `G`, and `B` satisfy all of the conditions below? Find the count modulo 998244353.

* The number of occurrences of `R`, `G`, and `B` in S are R, G, and B, respectively.
* The number of occurrences of `RG` as (contiguous) substrings in S is K.

### Constraints

* 1 \leq R,G,B\leq 10^6
* 0 \leq K \leq \mathrm{min}(R,G)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
R G B K
```

### Output

Print the answer.

---

### Sample Input 1

```
2 1 1 1
```

### Sample Output 1

```
6
```

The following six strings satisfy the conditions.

* `RRGB`
* `RGRB`
* `RGBR`
* `RBRG`
* `BRRG`
* `BRGR`

---

### Sample Input 2

```
1000000 1000000 1000000 1000000
```

### Sample Output 2

```
80957240
```

Find the count modulo 998244353.
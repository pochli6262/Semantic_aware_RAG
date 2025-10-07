Score : 100 points

### Problem Statement

Takahashi eats three plates for breakfast: rice, miso soup, and salad.

His table is long and narrow, so he arranged the three plates in a row. The arrangement is given by a string S, where the i-th plate from the left is rice if S\_i is `R`, miso soup if S\_i is `M`, and salad if S\_i is `S`.

Determine whether the plate of rice is to the left of the plate of miso soup.

### Constraints

* |S| = 3
* S contains one `R`, one `M`, and one `S`.

---

### Input

The input is given from Standard Input in the following format:

```
S
```

### Output

Print `Yes` if the plate of rice is to the left of the plate of miso soup, and `No` otherwise.

---

### Sample Input 1

```
RSM
```

### Sample Output 1

```
Yes
```

The plate of rice is at the 1st position from the left, and the plate of miso soup is at the 3rd position from the left. Since the plate of rice is to the left, print `Yes`.

---

### Sample Input 2

```
SMR
```

### Sample Output 2

```
No
```

The plates are arranged as salad, miso soup, and rice from left to right.
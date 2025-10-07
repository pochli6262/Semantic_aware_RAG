Score : 600 points

### Problem Statement

N people, numbered 1,2,\ldots ,N, are going to stand on the number line.
Let's denote by x\_i the coordinate the Person i stands at.
Then, x\_i should be an integer satisfying L\_i \leq x\_i \leq R\_i.
Multiple people can occupy the same coordinate.

We define the **dissatisfaction level** as the following formula:

> \displaystyle\sum\_{i=1}^{N-1}\sum\_{j=i+1}^{N}|x\_j-x\_i|

Find the minimum possible value of the dissatisfaction level.

### Constraints

* 2 \leq N \leq 3 \times 10^5
* 1 \leq L\_i \leq R\_i \leq 10^7 \,(1 \leq i \leq N)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
L_1 R_1
L_2 R_2
\vdots
L_N R_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
1 3
2 4
5 6
```

### Sample Output 1

```
4
```

If we let x\_1=3,x\_2=4,x\_3=5, we get the dissatisfaction level of 4. We cannot make it 3 or less, so the answer is 4.

---

### Sample Input 2

```
3
1 1
1 1
1 1
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
6
1 5
2 4
1 1
4 4
3 6
3 3
```

### Sample Output 3

```
15
```
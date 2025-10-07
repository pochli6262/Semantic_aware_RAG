Score: 200 points

### Problem Statement

Takahashi has N teeth, one in each of the holes numbered 1, 2, \dots, N.  
Dentist Aoki will perform Q treatments on these teeth and holes.  
In the i-th treatment, hole T\_i is treated as follows:

* If there is a tooth in hole T\_i, remove the tooth from hole T\_i.
* If there is no tooth in hole T\_i (i.e., the hole is empty), grow a tooth in hole T\_i.

After all treatments are completed, how many teeth does Takahashi have?

### Constraints

* All input values are integers.
* 1 \le N, Q \le 1000
* 1 \le T\_i \le N

---

### Input

The input is given from Standard Input in the following format:

```
N Q
T_1 T_2 \dots T_Q
```

### Output

Print the number of teeth as an integer.

---

### Sample Input 1

```
30 6
2 9 18 27 18 9
```

### Sample Output 1

```
28
```

Initially, Takahashi has 30 teeth, and Aoki performs six treatments.

* In the first treatment, hole 2 is treated. There is a tooth in hole 2, so it is removed.
* In the second treatment, hole 9 is treated. There is a tooth in hole 9, so it is removed.
* In the third treatment, hole 18 is treated. There is a tooth in hole 18, so it is removed.
* In the fourth treatment, hole 27 is treated. There is a tooth in hole 27, so it is removed.
* In the fifth treatment, hole 18 is treated. There is no tooth in hole 18, so a tooth is grown.
* In the sixth treatment, hole 9 is treated. There is no tooth in hole 9, so a tooth is grown.

The final count of teeth is 28.

---

### Sample Input 2

```
1 7
1 1 1 1 1 1 1
```

### Sample Output 2

```
0
```

---

### Sample Input 3

```
9 20
9 5 1 2 2 2 8 9 2 1 6 2 6 5 8 7 8 5 9 8
```

### Sample Output 3

```
5
```
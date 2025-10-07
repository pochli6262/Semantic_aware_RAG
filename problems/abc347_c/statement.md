Score: 350 points

### Problem Statement

In the Kingdom of AtCoder, a week consists of A+B days, with the first through A-th days being holidays and the (A+1)-th through (A+B)-th being weekdays.

Takahashi has N plans, and the i-th plan is scheduled D\_i days later.

He has forgotten what day of the week it is today. Determine if it is possible for all of his N plans to be scheduled on holidays.

### Constraints

* 1\leq N\leq 2\times 10^5
* 1\leq A,B\leq 10^9
* 1\leq D\_1<D\_2<\ldots<D\_N\leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N A B
D_1 D_2 \ldots D_N
```

### Output

Print `Yes` in a single line if it is possible for all of Takahashi's N plans to be scheduled on holidays, and `No` otherwise.

---

### Sample Input 1

```
3 2 5
1 2 9
```

### Sample Output 1

```
Yes
```

In this input, a week consists of seven days, with the first through second days being holidays and the third through seventh days being weekdays.

Let us assume today is the seventh day of the week. In this case, one day later would be the first day of the week, two days later would be the second day of the week, and nine days later would also be the second day of the week, making all plans scheduled on holidays. Therefore, it is possible for all of Takahashi's N plans to be scheduled on holidays.

---

### Sample Input 2

```
2 5 10
10 15
```

### Sample Output 2

```
No
```

---

### Sample Input 3

```
4 347 347
347 700 705 710
```

### Sample Output 3

```
Yes
```
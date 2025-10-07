Score : 600 points

### Problem Statement

We have a sequence of N terms: a\_1,a\_2,\ldots,a\_N.
You can perform the following operation on this sequence any number of times (possibly zero).

* Choose a term of the sequence at that point, and let s be its value.
  Then, for every 1\leq i\leq N, replace a\_i with 2s-a\_i.
  However, this operation may not be performed in a way that produces a term with a negative value.

You want to make the greatest value among the terms of the sequence as small as possible.
What will this value be after an optimal sequence of operations for this objective?

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq a\_1 < a\_2 < \ldots < a\_N \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
a_1 a_2 \ldots a_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3
1 3 6
```

### Sample Output 1

```
5
```

If you perform the operation with s=3, the sequence becomes (5,3,0). The greatest value here is 5.
Under the condition that there may not be a term with a negative value, the greatest value among the terms of the sequence cannot be made smaller, so you should print 5.

---

### Sample Input 2

```
5
400 500 600 700 800
```

### Sample Output 2

```
400
```

To obtain this result, perform the operation once with s=400, or perform it with s=500 and then with s=300, for instance.
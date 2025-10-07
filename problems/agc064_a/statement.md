Score : 400 points

### Problem Statement

You are given a positive integer N.
Print an integer sequence of length L \coloneqq N(N+1)/2, A = (A\_1, A\_2, \ldots, A\_L), that satisfies all of the following conditions.

* A contains exactly i occurrences of i for every i = 1, 2, \ldots, N.
* 1 \leq |A\_i - A\_{i+1}| \leq 2 for every i = 1, 2, \ldots, L. Here, A\_{L+1} means A\_1.

It can be proved that, under the Constraints of this problem, there is always an integer sequence A of length L that satisfies all of the above conditions.

### Constraints

* 3 \leq N \leq 1000
* N is an integer.

---

### Input

The input is given from Standard Input in the following format:

```
N
```

### Output

Print the elements of A, separated by spaces, in the following format:

```
A_1 A_2 \ldots A_L
```

If multiple integer sequences A of length L satisfy the conditions in the problem statement, any one of them is accepted.

---

### Sample Input 1

```
4
```

### Sample Output 1

```
1 3 4 2 4 3 4 2 4 3
```

The integer sequence A = (1, 3, 4, 2, 4, 3, 4, 2, 4, 3) contains exactly one 1, two 2s, three 3s, and four 4s, satisfying the first condition.
The second condition is also satisfied, as follows:

* |A\_1 - A\_2| = |1 - 3| = 2
* |A\_2 - A\_3| = |3 - 4| = 1
* |A\_3 - A\_4| = |4 - 2| = 2
* |A\_4 - A\_5| = |2 - 4| = 2
* |A\_5 - A\_6| = |4 - 3| = 1
* |A\_6 - A\_7| = |3 - 4| = 1
* |A\_7 - A\_8| = |4 - 2| = 2
* |A\_8 - A\_9| = |2 - 4| = 2
* |A\_9 - A\_{10}| = |4 - 3| = 1
* |A\_{10} - A\_1| = |3 - 1| = 2
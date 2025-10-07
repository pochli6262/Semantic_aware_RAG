Score : 400 points

### Problem Statement

You are given a sequence of non-negative integers A=(a\_1,a\_2,\ldots,a\_N).

Let S be the set of non-negative integers that can be the sum of K terms in A (with distinct indices).

Find the greatest multiple of D in S. If there is no multiple of D in S, print `-1` instead.

### Constraints

* 1 \leq K \leq N \leq 100
* 1 \leq D \leq 100
* 0 \leq a\_i \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N K D
a_1 \ldots a_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2 2
1 2 3 4
```

### Sample Output 1

```
6
```

Here are all the ways to choose two terms in A.

* Choose a\_1 and a\_2, whose sum is 1+2=3.
* Choose a\_1 and a\_3, whose sum is 1+3=4.
* Choose a\_1 and a\_4, whose sum is 1+4=5.
* Choose a\_2 and a\_3, whose sum is 2+3=5.
* Choose a\_2 and a\_4, whose sum is 2+4=6.
* Choose a\_3 and a\_4, whose sum is 3+4=7.

Thus, we have S=\{3,4,5,6,7\}. The greatest multiple of 2 in S is 6, so you should print 6.

---

### Sample Input 2

```
3 1 2
1 3 5
```

### Sample Output 2

```
-1
```

In this example, we have S=\{1,3,5\}. Nothing in S is a multiple of 2, so you should print `-1`.
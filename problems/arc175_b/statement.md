Score: 400 points

### Problem Statement

You are given a string S of length 2N consisting of the characters `(` and `)`. Let S\_i denote the i-th character from the left of S.

You can perform the following two types of operations zero or more times in any order:

* Choose a pair of integers (i,j) such that 1\leq i < j \leq 2N. Swap S\_i and S\_j. The cost of this operation is A.
* Choose an integer i such that 1\leq i \leq 2N. Replace S\_i with `(` or `)`. The cost of this operation is B.

Your goal is to make S a correct parenthesis sequence. Find the minimum total cost required to achieve this goal. It can be proved that the goal can always be achieved with a finite number of operations.

What is a correct parenthesis sequence?
A correct parenthesis sequence is a string that satisfies any of the following conditions:

* It is an empty string.
* It is formed by concatenating `(`, A, `)` in this order where A is a correct parenthesis sequence.
* It is formed by concatenating A and B in this order where A and B are correct parenthesis sequences.

### Constraints

* All input values are integers.
* 1 \leq N \leq 5\times 10^5
* 1\leq A,B\leq 10^9
* S is a string of length 2N consisting of the characters `(` and `)`.

---

### Input

The Input is given from Standard Input in the following format:

```
N A B
S
```

### Output

Print the answer in a single line.

---

### Sample Input 1

```
3 3 2
)))(()
```

### Sample Output 1

```
5
```

Here is one way to operate:

* Swap S\_3 and S\_4. S becomes `))()()`. The cost is 3.
* Replace S\_1 with `(`. S becomes `()()()`, which is a correct parentheses sequence. The cost is 2.

In this case, we have made S a correct bracket sequence for a total cost of 5. There is no way to make S a correct bracket sequence for less than 5.

---

### Sample Input 2

```
1 175 1000000000
()
```

### Sample Output 2

```
0
```

The given S is already a correct bracket sequence, so no operation is needed.

---

### Sample Input 3

```
7 2622 26092458
))()((((()()((
```

### Sample Output 3

```
52187538
```
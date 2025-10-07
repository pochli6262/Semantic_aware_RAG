Score : 400 points

### Problem Statement

You are given a string S of length N consisting of characters `A` and `B`.

You can perform the following two types of operations zero or more times in any order:

* Choose a (contiguous) substring `ABA` in S and replace it with `A`.
* Choose a (contiguous) substring `BAB` in S and replace it with `B`.

Find, modulo 10^9+7, the number of possible strings S after performing the operations.

### Constraints

* 1 \leq N \leq 250000
* S is a string of length N consisting of characters `A` and `B`.

---

### Input

The input is given from Standard Input in the following format:

```
N
S
```

### Output

Print the answer.

---

### Sample Input 1

```
4
ABAB
```

### Sample Output 1

```
2
```

The two possible strings S after the operations are as follows:

* `ABAB`: This string can be obtained by performing zero operations.
* `AB`: The 1st to 3rd characters of S=`ABAB` are `ABA`. Replacing them with `A` results in S=`AB`.

Here, the 2nd to 4th characters of S=`ABAB` are `BAB`, so you can also replace them with `B`. Note, however, that the resulting `AB` does not count multiple times.

---

### Sample Input 2

```
1
A
```

### Sample Output 2

```
1
```

No operations can be performed.

---

### Sample Input 3

```
17
BBABABAABABAAAABA
```

### Sample Output 3

```
18
```

---

### Sample Input 4

```
100
ABAABAABABBABAABAABAABABBABBABBABBABBABBABBABBABBABBABBABBABBABBABAABABAABABBABBABABBABAABAABAABAABA
```

### Sample Output 4

```
415919090
```

Remember to take the result modulo 10^9+7.
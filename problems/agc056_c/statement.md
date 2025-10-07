Score : 900 points

### Problem Statement

Consider making a string s of length N consisting of `0` and `1`, where s must satisfy M conditions.
The i-th condition is represented by integers L\_i and R\_i (1 \leq L\_i < R\_i \leq N).
This means that there should be equal numbers of `0` and `1` between the L\_i-th and R\_i-th characters (inclusive) of s.

Find the lexicographically smallest string s that satisfies all conditions.
It can be proved that the Constraints of the problem guarantee the existence of s that satisfies the conditions.

### Constraints

* 2 \leq N \leq 10^6
* 1 \leq M \leq 200000
* 1 \leq L\_i < R\_i \leq N
* (R\_i-L\_i+1) \equiv 0 \mod 2
* (L\_i,R\_i) \neq (L\_j,R\_j) (i \neq j)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
L_1 R_1
L_2 R_2
\vdots
L_M R_M
```

### Output

Print the answer.

---

### Sample Input 1

```
4 2
1 2
3 4
```

### Sample Output 1

```
0101
```

---

### Sample Input 2

```
6 2
1 4
3 6
```

### Sample Output 2

```
001100
```

---

### Sample Input 3

```
20 10
6 17
2 3
14 19
5 14
10 15
7 20
10 19
3 20
6 9
7 12
```

### Sample Output 3

```
00100100101101001011
```
Score : 300 points

### Problem Statement

A region has N towns numbered 1 to N, and M roads numbered 1 to M.

The i-th road connects town A\_i and town B\_i bidirectionally with length C\_i.

Find the maximum possible total length of the roads you traverse when starting from a town of your choice and getting to another town without passing through the same town more than once.

### Constraints

* 2 \leq N \leq 10
* 1 \leq M \leq \frac{N(N-1)}{2}
* 1 \leq A\_i < B\_i \leq N
* The pairs (A\_i,B\_i) are distinct.
* 1\leq C\_i \leq 10^8
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 B_1 C_1
\vdots
A_M B_M C_M
```

### Output

Print the answer.

---

### Sample Input 1

```
4 4
1 2 1
2 3 10
1 3 100
1 4 1000
```

### Sample Output 1

```
1110
```

If you travel as 4\to 1\to 3\to 2, the total length of the roads you traverse is 1110.

---

### Sample Input 2

```
10 1
5 9 1
```

### Sample Output 2

```
1
```

There may be a town that is not connected to a road.

---

### Sample Input 3

```
10 13
1 2 1
1 10 1
2 3 1
3 4 4
4 7 2
4 8 1
5 8 1
5 9 3
6 8 1
6 9 5
7 8 1
7 9 4
9 10 3
```

### Sample Output 3

```
20
```

![Figure](https://img.atcoder.jp/abc317/06ac62d13dd1c4b2b469a524a60eb093.png)
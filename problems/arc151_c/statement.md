Score : 600 points

### Problem Statement

There are N squares called square 1, square 2, \ldots, square N, where square i and square i+1 are adjacent for each i = 1, 2, \ldots, N-1.

Initially, M of the squares have 0 or 1 written on them.
Specifically, for each i = 1, 2, \ldots, M, Y\_i is written on square X\_i.
The other N-M squares have nothing written on them.

Takahashi and Aoki will play a game against each other.
The two will alternately act as follows, with Takahashi going first.

* Choose a square with nothing written yet, and write 0 or 1 on that square.
  Here, it is forbidden to make two adjacent squares have the same digit written on them.

The first player to be unable to act loses; the other player wins.

Determine the winner when both players adopt the optimal strategy for their own victory.

### Constraints

* 1 \leq N \leq 10^{18}
* 0 \leq M \leq \min\lbrace N, 2 \times 10^5 \rbrace
* 1 \leq X\_1 \lt X\_2 \lt \cdots \lt X\_M \leq N
* Y\_i \in \lbrace 0, 1\rbrace
* X\_i + 1 = X\_{i+1} \implies Y\_i \neq Y\_{i+1}
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
X_1 Y_1
X_2 Y_2
\vdots
X_M Y_M
```

### Output

If Takahashi wins, print `Takahashi`; if Aoki wins, print `Aoki`.

---

### Sample Input 1

```
7 2
2 0
4 1
```

### Sample Output 1

```
Takahashi
```

Here is one possible progression of the game.

1. Takahashi writes 0 on square 6.
2. Aoki writes 1 on square 1.
3. Takahashi writes 1 on square 7.

Then, Aoki cannot write 0 or 1 on any square, so Takahashi wins.

---

### Sample Input 2

```
3 3
1 1
2 0
3 1
```

### Sample Output 2

```
Aoki
```

Since every square already has 0 or 1 written at the beginning, Takahashi, who goes first, cannot act, so Aoki wins.

---

### Sample Input 3

```
1000000000000000000 0
```

### Sample Output 3

```
Aoki
```
Score : 300 points

### Problem Statement

On a two-dimensional plane, Takahashi is initially at point (0, 0), and his initial health is H. M items to recover health are placed on the plane; the i-th of them is placed at (x\_i,y\_i).

Takahashi will make N moves. The i-th move is as follows.

1. Let (x,y) be his current coordinates. He consumes a health of 1 to move to the following point, depending on S\_i, the i-th character of S:

   * (x+1,y) if S\_i is `R`;
   * (x-1,y) if S\_i is `L`;
   * (x,y+1) if S\_i is `U`;
   * (x,y-1) if S\_i is `D`.
2. If Takahashi's health has become negative, he collapses and stops moving. Otherwise, if an item is placed at the point he has moved to, and his health is strictly less than K, then he consumes the item there to make his health K.

Determine if Takahashi can complete the N moves without being stunned.

### Constraints

* 1\leq N,M,H,K\leq 2\times 10^5
* S is a string of length N consisting of `R`, `L`, `U`, and `D`.
* |x\_i|,|y\_i| \leq 2\times 10^5
* (x\_i, y\_i) are pairwise distinct.
* All values in the input are integers, except for S.

---

### Input

The input is given from Standard Input in the following format:

```
N M H K
S
x_1 y_1
\vdots
x_M y_M
```

### Output

Print `Yes` if he can complete the N moves without being stunned; print `No` otherwise.

---

### Sample Input 1

```
4 2 3 1
RUDL
-1 -1
1 0
```

### Sample Output 1

```
Yes
```

Initially, Takahashi's health is 3. We describe the moves below.

* 1-st move: S\_i is `R`, so he moves to point (1,0). His health reduces to 2. Although an item is placed at point (1,0), he do not consume it because his health is no less than K=1.
* 2-nd move: S\_i is `U`, so he moves to point (1,1). His health reduces to 1.
* 3-rd move: S\_i is `D`, so he moves to point (1,0). His health reduces to 0. An item is placed at point (1,0), and his health is less than K=1, so he consumes the item to make his health 1.
* 4-th move: S\_i is `L`, so he moves to point (0,0). His health reduces to 0.

Thus, he can make the 4 moves without collapsing, so `Yes` should be printed. Note that the health may reach 0.

---

### Sample Input 2

```
5 2 1 5
LDRLD
0 0
-1 -1
```

### Sample Output 2

```
No
```

Initially, Takahashi's health is 1. We describe the moves below.

* 1-st move: S\_i is `L`, so he moves to point (-1,0). His health reduces to 0.
* 2-nd move: S\_i is `D`, so he moves to point (-1,-1). His health reduces to -1. Now that the health is -1, he collapses and stops moving.

Thus, he will be stunned, so `No` should be printed.

Note that although there is an item at his initial point (0,0), he does not consume it before the 1-st move, because items are only consumed after a move.
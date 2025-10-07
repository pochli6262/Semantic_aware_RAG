Score : 550 points

### Problem Statement

You are given an integer sequence A = (A\_1, A\_2, \ldots, A\_N) of length N.

We will perform the following operation on A for i = 1, 2, \ldots, M in this order.

* First, choose an integer between L\_i and R\_i, inclusive, uniformly at random and denote it as p.
* Then, change the value of A\_p to the integer X\_i.

For the final sequence A after the above procedure, print the expected value, modulo 998244353, of A\_i for each i = 1, 2, \ldots, N.

 How to print expected values modulo 998244353

It can be proved that the expected values sought in this problem are always rational. Furthermore, the constraints of this problem guarantee that if each of those expected values is expressed as an irreducible fraction \frac{y}{x}, then x is not divisible by 998244353.

Now, there is a unique integer z between 0 and 998244352, inclusive, such that xz \equiv y \pmod{998244353}. Report this z.

### Constraints

* All input values are integers.
* 1 \leq N, M \leq 2 \times 10^5
* 0 \leq A\_i \leq 10^9
* 1 \leq L\_i \leq R\_i \leq N
* 0 \leq X\_i \leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 A_2 \ldots A_N
L_1 R_1 X_1
L_2 R_2 X_2
\vdots
L_M R_M X_M
```

### Output

Print the expected values E\_i of the final A\_i for i = 1, 2, \ldots, N in the format below, separated by spaces.

```
E_1 E_2 \ldots E_N
```

---

### Sample Input 1

```
5 2
3 1 4 1 5
1 2 2
2 4 0
```

### Sample Output 1

```
499122179 1 665496238 665496236 5
```

We start from the initial state A = (3, 1, 4, 1, 5) and perform the following two operations.

* The first operation chooses A\_1 or A\_2 uniformly at random, and changes its value to 2.
* Then, the second operation chooses one of A\_2, A\_3, A\_4 uniformly at random, and changes its value to 0.

As a result, the expected values of the elements in the final A are (E\_1, E\_2, E\_3, E\_4, E\_5) = (\frac{5}{2}, 1, \frac{8}{3}, \frac{2}{3}, 5).

---

### Sample Input 2

```
2 4
1 2
1 1 3
2 2 4
1 1 5
2 2 6
```

### Sample Output 2

```
5 6
```

---

### Sample Input 3

```
20 20
998769066 273215338 827984962 78974225 994243956 791478211 891861897 680427073 993663022 219733184 570206440 43712322 66791680 164318676 209536492 137458233 289158777 461179891 612373851 330908158
12 18 769877494
9 13 689822685
6 13 180913148
2 16 525285434
2 14 98115570
14 17 622616620
8 12 476462455
13 17 872412050
14 15 564176146
7 13 143650548
2 5 180435257
4 10 82903366
1 2 643996562
8 10 262860196
10 14 624081934
11 13 581257775
9 19 381806138
3 12 427930466
6 19 18249485
14 19 682428942
```

### Sample Output 3

```
821382814 987210378 819486592 142238362 447960587 678128197 687469071 405316549 318941070 457450677 426617745 712263899 939619994 228431878 307695685 196179692 241456697 12668393 685902422 330908158
```
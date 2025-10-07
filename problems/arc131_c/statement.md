Score : 600 points

### Problem Statement

There are N cookies on a desk. Each cookie has a positive integer on its surface: A\_1, A\_2, \dots, A\_N, which are all different.

Let us play a game with two players using these cookies. In this game, the players alternately do the following action.

> Choose a cookie on the desk and eat it.
> Then, if the \mathrm{XOR} of the integers written on the remaining cookies on the desk becomes 0, the player wins, and the game ends.

You have asked the boy E869120 to play this game with you. You go first, and E869120 goes second. Are you going to win if both players play optimally?

What is \mathrm{XOR}?

The bitwise \mathrm{XOR} of integers A and B, A\ \mathrm{XOR}\ B, is defined as follows:

* When A\ \mathrm{XOR}\ B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if exactly one of A and B is 1, and 0 otherwise.

For example, we have 3\ \mathrm{XOR}\ 5 = 6 (in base two: 011\ \mathrm{XOR}\ 101 = 110).  
Generally, the bitwise \mathrm{XOR} of k integers p\_1, p\_2, p\_3, \dots, p\_k is defined as (\dots ((p\_1\ \mathrm{XOR}\ p\_2)\ \mathrm{XOR}\ p\_3)\ \mathrm{XOR}\ \dots\ \mathrm{XOR}\ p\_k). We can prove that this value does not depend on the order of p\_1, p\_2, p\_3, \dots p\_k. Particularly, when k = 0, the \mathrm{XOR} is 0.

### Constraints

* 1 \leq N \leq 400000
* 1 \leq A\_i \leq 10^9 \ (1 \leq i \leq N)
* A\_1, A\_2, \dots, A\_N are all different.
* The \mathrm{XOR} of A\_1, A\_2, \dots, A\_N is not 0.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 A_2 \cdots A_N
```

### Output

If you are going to win if both players play optimally, print `Win`; if you are going to lose, print `Lose`.

---

### Sample Input 1

```
6
9 14 11 3 5 8
```

### Sample Output 1

```
Lose
```

In this case, regardless of what choices you make, you will lose if E869120 keeps playing optimally.

For example, let us say you first eat the cookie with 11 written on it. Then, E869120 will eat the cookie with 9 so that the \mathrm{XOR} of the numbers written on the remaining cookies, 14, 3, 5, 8, is 0, making him win.

Even if you make other choices, E869120 will win eventually.

---

### Sample Input 2

```
1
131
```

### Sample Output 2

```
Win
```

In this case, your only choice in your first turn is to eat the cookie with 131. Then, there is no more cookie on the desk, making the \mathrm{XOR} of the numbers written on the remaining cookies 0. Therefore, before E869120 gets to do anything, you win.

---

### Sample Input 3

```
8
12 23 34 45 56 78 89 98
```

### Sample Output 3

```
Win
```
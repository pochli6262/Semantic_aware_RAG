Score : 600 points

### Problem Statement

There is a length L string S consisting of uppercase and lowercase English letters displayed on an electronic bulletin board with a width of W. The string S scrolls from right to left by a width of one character at a time.

The display repeats a cycle of L+W-1 states, with the first character of S appearing from the right edge when the last character of S disappears from the left edge.

For example, when W=5 and S= `ABC`, the board displays the following seven states in a loop:

* `ABC..`
* `BC...`
* `C....`
* `....A`
* `...AB`
* `..ABC`
* `.ABC.`

(`.` represents a position where no character is displayed.)

More precisely, there are distinct states for k=0,\ldots,L+W-2 in which the display is as follows.

* Let f(x) be the remainder when x is divided by L+W-1. The (i+1)-th position from the left of the board displays the (f(i+k)+1)-th character of S when f(i+k)<L, and nothing otherwise.

You are given a length W string P consisting of uppercase English letters, lowercase English letters, `.`, and `_`.  
Find the number of states among the L+W-1 states of the board that coincide P except for the positions with `_`.  
More precisely, find the number of states that satisfy the following condition.

* For every i=1,\ldots,W, one of the following holds.
  + The i-th character of P is `_`.
  + The character displayed at the i-th position from the left of the board is equal to the i-th character of P.
  + Nothing is displayed at the i-th position from the left of the board, and the i-th character of P is `.`.

### Constraints

* 1 \leq L \leq W \leq 3\times 10^5
* L and W are integers.
* S is a string of length L consisting of uppercase and lowercase English letters.
* P is a string of length W consisting of uppercase and lowercase English letters, `.`, and `_`.

---

### Input

The input is given from Standard Input in the following format:

```
L W
S
P
```

### Output

Print the answer.

---

### Sample Input 1

```
3 5
ABC
..___
```

### Sample Output 1

```
3
```

There are three desired states, where the board displays `....A`, `...AB`, `..ABC`.

---

### Sample Input 2

```
11 15
abracadabra
__.._________ab
```

### Sample Output 2

```
2
```

---

### Sample Input 3

```
20 30
abaababbbabaabababba
__a____b_____a________________
```

### Sample Output 3

```
2
```

---

### Sample Input 4

```
1 1
a
_
```

### Sample Output 4

```
1
```
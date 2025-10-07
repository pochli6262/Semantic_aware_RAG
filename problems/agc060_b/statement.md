Score : 700 points

### Problem Statement

We have a grid with N rows and M columns.
You want to write an integer between 0 and 2^K-1 in each square in the grid to satisfy the following condition.

* Consider a path that starts at the top-left square, repeatedly moves right or down to an adjacent square, and ends at the bottom-right square.
  Such a path is said to be **good** if and only if the total \mathrm{XOR} of the integers written on the squares visited (including the starting and ending points) is 0.
* There is exactly one good path, which is the path represented by a string S.
  The path represented by the string S is a path that, for each i (1 \leq i \leq N+M-2), the i-th move is right if the i-th character of S is `R` and down if that character is `D`.

Determine whether there is a way to write integers that satisfies the condition.

For each input file, solve T test cases.

What is bitwise \mathrm{XOR}?

The bitwise \mathrm{XOR} of non-negative integers A and B, A \oplus B, is defined as follows.

* When A \oplus B is written in binary, the k-th lowest bit (k \geq 0) is 1 if exactly one of the k-th lowest bits of A and B is 1, and 0 otherwise.

For instance, 3 \oplus 5 = 6 (in binary: 011 \oplus 101 = 110).  
Generally, the bitwise \mathrm{XOR} of k non-negative integers p\_1, p\_2, p\_3, \dots, p\_k is defined as (\dots ((p\_1 \oplus p\_2) \oplus p\_3) \oplus \dots \oplus p\_k), which can be proved to be independent of the order of p\_1, p\_2, p\_3, \dots, p\_k.

### Constraints

* 1 \leq T \leq 100
* 2 \leq N,M \leq 30
* 1 \leq K \leq 30
* S is a string containing exactly N-1 `D`s and M-1 `R`s.
* All numbers in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
T
case_1
case_2
\vdots
case_T
```

Each case is in the following format:

```
N M K
S
```

### Output

For each case, print `Yes` if there is a way to write integers that satisfies the condition, and `No` otherwise.
Each character in the output may be either uppercase or lowercase.

---

### Sample Input 1

```
4
2 2 1
RD
4 3 1
RDDDR
15 20 18
DDRRRRRRRDDDDRRDDRDRRRRDDRDRDDRRR
20 15 7
DRRDDDDDRDDDRRDDRRRDRRRDDDDDRRRDD
```

### Sample Output 1

```
Yes
No
Yes
No
```

As an example, for the first case, you can make the grid as follows.

```
11
00
```
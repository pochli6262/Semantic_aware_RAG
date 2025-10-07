Score : 525 points

### Problem Statement

There is a row of N squares labeled 1,2,\dots,N and a sequence A=(A\_1,A\_2,\dots,A\_N) of length N.  
Initially, square 1 is painted black, the other N-1 squares are painted white, and a piece is placed on square 1.

You may repeat the following operation any number of times, possibly zero:

* When the piece is on square i, choose a positive integer x and move the piece to square i + A\_i \times x.
  + Here, you cannot make a move with i + A\_i \times x > N.
* Then, paint the square i + A\_i \times x black.

Find the number of possible sets of squares that can be painted black at the end of the operations, modulo 998244353.

### Constraints

* All input values are integers.
* 1 \le N \le 2 \times 10^5
* 1 \le A\_i \le 2 \times 10^5

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
5
1 2 3 1 1
```

### Sample Output 1

```
8
```

There are eight possible sets of squares painted black:

* Square 1
* Squares 1,2
* Squares 1,2,4
* Squares 1,2,4,5
* Squares 1,3
* Squares 1,4
* Squares 1,4,5
* Squares 1,5

---

### Sample Input 2

```
1
200000
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
40
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

### Sample Output 3

```
721419738
```

Be sure to find the number modulo 998244353.
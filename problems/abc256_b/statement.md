Score : 200 points

### Problem Statement

> Takahashi is trying to create a game inspired by baseball, but he is having difficulty writing the code.  
> Write a program for Takahashi that solves the following problem.

There are 4 squares called Square 0, Square 1, Square 2, and Square 3. Initially, all squares are empty.  
There is also an integer P; initially, P = 0.  
Given a sequence of positive integers A = (A\_1, A\_2, \dots, A\_N), perform the following operations for i = 1, 2, \dots, N in this order:

1. Put a piece on Square 0.
2. Advance every piece on the squares A\_i squares ahead. In other words, if Square x has a piece, move the piece to Square (x + A\_i).   
   If, however, the destination square does not exist (i.e. x + A\_i is greater than or equal to 4) for a piece, remove it. Add to P the number of pieces that have been removed.

Print the value of P after all the operations have been performed.

### Constraints

* 1 \leq N \leq 100
* 1 \leq A\_i \leq 4
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
A_1 A_2 \dots A_N
```

### Output

Print the value of P after all the operations have been performed.

---

### Sample Input 1

```
4
1 1 3 2
```

### Sample Output 1

```
3
```

The operations are described below. After all the operations have been performed, P equals 3.

* The operations for i=1:
  1. Put a piece on Square 0. Now, Square 0 has a piece.
  2. Advance every piece on the squares 1 square ahead. After these moves, Square 1 has a piece.
* The operations for i=2:
  1. Put a piece on Square 0. Now, Squares 0 and 1 have a piece.
  2. Advance every piece on the squares 1 square ahead. After these moves, Squares 1 and 2 have a piece.
* The operations for i=3:
  1. Put a piece on Square 0. Now, Squares 0, 1, and 2 have a piece.
  2. Advance every piece on the squares 3 squares ahead.  
     Here, for the pieces on Squares 1 and 2, the destination squares do not exist (since 1+3=4 and 2+3=5), so remove these pieces and add 2 to P. P now equals 2.
     After these moves, Square 3 has a piece.
* The operations for i=4:
  1. Put a piece on Square 0. Now, Squares 0 and 3 have a piece.
  2. Advance every piece on the squares 2 squares ahead.  
     Here, for the piece on Square 3, the destination square does not exist (since 3+2=5), so remove this piece and add 1 to P. P now equals 3.  
     After these moves, Square 2 has a piece.

---

### Sample Input 2

```
3
1 1 1
```

### Sample Output 2

```
0
```

The value of P may not be updated by the operations.

---

### Sample Input 3

```
10
2 2 4 1 1 1 4 2 2 1
```

### Sample Output 3

```
8
```
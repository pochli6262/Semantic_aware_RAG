Score : 600 points

### Problem Statement

There is an empty sequence X and an empty stack S. Also, you are given an integer sequence A=(a\_1,\ldots,a\_N) of length N.  
For each i=1,\ldots,N in this order, Takahashi will do one of the following operations:

* Move the integer a\_i onto the top of S.
* Discard the integer a\_i from A.

Additionally, Takahashi may do the following operation whenever S is not empty:

* Move the integer at the top of S to the tail of X.

The score of the final X is defined as follows.

* If X is non-decreasing, i.e. if x\_i \leq x\_{i+1} holds for all integer i(1 \leq i \lt |X|), where X=(x\_1,\ldots,x\_{|X|}), then the score is |X| (where |X| denotes the number of terms in X).
* If X is not non-decreasing, then the score is 0.

Find the maximum possible score.

### Constraints

* 1 \leq N \leq 50
* 1 \leq a\_i \leq 50
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
a_1 \ldots a_N
```

### Output

Print the answer.

---

### Sample Input 1

```
7
1 2 3 4 1 2 3
```

### Sample Output 1

```
5
```

The following operations make the final X equal (1,1,2,3,4), for a score of 5.

* Move a\_1=1 onto the top of S.
* Move 1 at the top of S to the tail of X.
* Move a\_2=2 onto the top of S.
* Discard a\_3=3.
* Move a\_4=4 onto the top of S.
* Move a\_5=1 onto the top of S.
* Move 1 at the top of S to the tail of X.
* Move a\_6=2 onto the top of S.
* Move 2 at the top of S to the tail of X.
* Move a\_7=3 onto the top of S.
* Move 3 at the top of S to the tail of X.
* Move 4 at the top of S to the tail of X.

We cannot make the score 6 or greater, so the maximum possible score is 5.

---

### Sample Input 2

```
10
1 1 1 1 1 1 1 1 1 1
```

### Sample Output 2

```
10
```
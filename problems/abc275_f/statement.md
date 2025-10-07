Score : 500 points

### Problem Statement

You are given an integer array A=(a\_1,a\_2,\ldots,a\_N).  
You may perform the following operation any number of times (possibly zero).

* Choose a nonempty contiguous subarray of A, and delete it from the array.

For each x=1,2,\ldots,M, solve the following problem:

* Find the minimum possible number of operations to make the sum of elements of A equal x.
  If it is impossible to make the sum of elements of A equal x, print `-1` instead.

Note that the sum of elements of an empty array is 0.

### Constraints

* 1 \leq N,M \leq 3000
* 1 \leq a\_i \leq 3000
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
a_1 \ldots a_N
```

### Output

Print M lines. The i-th line should contain the answer for x=i.

---

### Sample Input 1

```
4 5
1 2 3 4
```

### Sample Output 1

```
1
2
1
1
1
```

The followings are examples of minimum number of operations that achieve the goal.

* For x=1, delete a\_2,a\_3,a\_4, and the sum of elements of A becomes x.
* For x=2, delete a\_3,a\_4, then delete a\_1, and the sum of elements of A becomes x.
* For x=3, delete a\_3,a\_4, and the sum of elements of A becomes x.
* For x=4, delete a\_1,a\_2,a\_3, and the sum of elements of A becomes x.
* For x=5, delete a\_2,a\_3, and the sum of elements of A becomes x.

---

### Sample Input 2

```
1 5
3
```

### Sample Output 2

```
-1
-1
0
-1
-1
```

---

### Sample Input 3

```
12 20
2 5 6 5 2 1 7 9 7 2 5 5
```

### Sample Output 3

```
2
1
2
2
1
2
1
2
2
1
2
1
1
1
2
2
1
1
1
1
```
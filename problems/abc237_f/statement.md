Score : 500 points

### Problem Statement

Find the number of sequences that satisfy all of the conditions below, modulo 998244353.

* The length is N.
* Each of the elements is an integer between 1 and M (inclusive).
* Its longest increasing subsequence has the length of exactly 3.

### Notes

A **subsequence** of a sequence is the result of removing zero or more elements from it and concatenating the remaining elements without changing the order.
For example, (10,30) is a subsequence of (10,20,30), while (20,10) is not a subsequence of (10,20,30).

A **longest increasing subsequence** of a sequence is its **strictly** increasing subsequence with the greatest length.

### Constraints

* 3 \leq N \leq 1000
* 3 \leq M \leq 10
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
```

### Output

Print the answer.

---

### Sample Input 1

```
4 5
```

### Sample Output 1

```
135
```

One sequence that satisfies the conditions is (3,4,1,5).  
On the other hand, (4,4,1,5) do not, because its longest increasing subsequence has the length of 2.

---

### Sample Input 2

```
3 4
```

### Sample Output 2

```
4
```

---

### Sample Input 3

```
111 3
```

### Sample Output 3

```
144980434
```

Find the count modulo 998244353.
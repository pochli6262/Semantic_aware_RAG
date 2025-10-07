Score : 600 points

### Problem Statement

You are given a sequence A=(A\_1,A\_2,\dots,A\_N) of length N.

Find the number, modulo 998244353, of ways to choose an odd number of elements from A so that the sum of the chosen elements equals M.

Two choices are said to be different if there exists an integer i (1 \le i \le N) such that one chooses A\_i but the other does not.

### Constraints

* 1 \le N \le 10^5
* 1 \le M \le 10^6
* 1 \le A\_i \le 10
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M
A_1 A_2 \dots A_N
```

### Output

Print the answer.

---

### Sample Input 1

```
5 6
1 2 3 3 6
```

### Sample Output 1

```
3
```

The following 3 choices satisfy the condition:

* Choosing A\_1, A\_2, and A\_3.
* Choosing A\_1, A\_2, and A\_4.
* Choosing A\_5.

Choosing A\_3 and A\_4 does not satisfy the condition because, although the sum is 6, the number of chosen elements is not odd.

---

### Sample Input 2

```
10 23
1 2 3 4 5 6 7 8 9 10
```

### Sample Output 2

```
18
```
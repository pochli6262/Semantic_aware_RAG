Score : 300 points

### Problem Statement

You have N keys numbered 1, 2, \dots, N.  
Some of these are real keys, while the others are dummies.

There is a door, Door X, into which you can insert any number of keys. Door X will open if and only if at least K real keys are inserted.

You have conducted M tests on these keys. The i-th test went as follows:

* You inserted C\_i keys A\_{i,1}, A\_{i,2}, \dots, A\_{i,C\_i} into Door X.
* The test result is represented by a single English letter R\_i.
  + R\_i = `o` means that Door X opened in the i-th test.
  + R\_i = `x` means that Door X did not open in the i-th test.

There are 2^N possible combinations of which keys are real and which are dummies. Among these, find the number of combinations that do not contradict any of the test results.  
It is possible that the given test results are incorrect and no combination satisfies the conditions. In such a case, report 0.

### Constraints

* N, M, K, C\_i, and A\_{i,j} are integers.
* 1 \le K \le N \le 15
* 1 \le M \le 100
* 1 \le C\_i \le N
* 1 \le A\_{i,j} \le N
* A\_{i,j} \neq A\_{i,k} if j \neq k.
* R\_i is `o` or `x`.

---

### Input

The input is given from Standard Input in the following format:

```
N M K
C_1 A_{1,1} A_{1,2} \dots A_{1,C_1} R_1
C_2 A_{2,1} A_{2,2} \dots A_{2,C_2} R_2
\vdots
C_M A_{M,1} A_{M,2} \dots A_{M,C_M} R_M
```

### Output

Print the answer as an integer.

---

### Sample Input 1

```
3 2 2
3 1 2 3 o
2 2 3 x
```

### Sample Output 1

```
2
```

In this input, there are three keys and two tests were conducted.  
Two correct keys are required to open Door X.

* In the first test, keys 1, 2, 3 were used, and Door X opened.
* In the second test, keys 2, 3 were used, and Door X did not open.

There are two combinations of which keys are real and which are dummies that do not contradict any of the test results:

* Key 1 is real, key 2 is a dummy, and key 3 is real.
* Key 1 is real, key 2 is real, and key 3 is a dummy.

---

### Sample Input 2

```
4 5 3
3 1 2 3 o
3 2 3 4 o
3 3 4 1 o
3 4 1 2 o
4 1 2 3 4 x
```

### Sample Output 2

```
0
```

As mentioned in the problem statement, the answer may be 0.

---

### Sample Input 3

```
11 4 9
10 1 2 3 4 5 6 7 8 9 10 o
11 1 2 3 4 5 6 7 8 9 10 11 o
10 11 10 9 8 7 6 5 4 3 2 x
10 11 9 1 4 3 7 5 6 2 10 x
```

### Sample Output 3

```
8
```
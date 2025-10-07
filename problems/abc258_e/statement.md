Score : 500 points

### Problem Statement

10^{100} potatoes are coming from a conveyor belt one by one. The weights of the potatoes are described by a sequence W = (W\_0, \dots, W\_{N-1}) of length N: the weight of the i-th potato coming is W\_{(i-1) \bmod N}, where (i-1) \bmod N denotes the remainder when i - 1 is divided by N.

Takahashi will prepare an empty box and then pack the potatoes in order, as follows.

* Pack the incoming potato into the box. If the total weight of the potatoes in the box is now X or greater, seal that box and prepare a new empty box.

You are given Q queries. In the i-th query (1 \leq i \leq Q), given a positive integer K\_i, find the number of potatoes in the K\_i-th box to be sealed. It can be proved that, under the Constraints of the problem, there will be at least K\_i sealed boxes.

### Constraints

* 1 \leq N, Q \leq 2 \times 10^5
* 1 \leq X \leq 10^9
* 1 \leq W\_i \leq 10^9 \, (0 \leq i \leq N - 1)
* 1 \leq K\_i \leq 10^{12} \, (1 \leq i \leq Q)
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N Q X
W_0 W_1 \ldots W_{N-1}
K_1
\vdots
K_Q
```

### Output

Print Q lines. The i-th line (1 \leq i \leq Q) should contain the answer to the i-th query.

---

### Sample Input 1

```
3 2 5
3 4 1
1
2
```

### Sample Output 1

```
2
3
```

Before sealing the 2-nd box, Takahashi will do the following:

* Prepare an empty box.
* Pack the 1-st potato into the box. Now, the total weight of potatoes in the box is 3.
* Pack the 2-nd potato into the box. Now, the total weight of potatoes in the box is 3 + 4 = 7, which is not less than X = 5, so seal this box.
* Prepare a new empty box.
* Pack the 3-rd potato into the box. Now, the total weight of potatoes in the box is 1.
* Pack the 4-th potato into the box. Now, the total weight of potatoes in the box is 1 + 3 = 4.
* Pack the 5-th potato into the box. Now, the total weight of potatoes in the box is 1 + 3 + 4 = 8, which is not less than X = 5, so seal this box.

The 1-st box sealed contains 2 potatoes, and the 2-nd box sealed contains 3 potatoes.

---

### Sample Input 2

```
10 5 20
5 8 5 9 8 7 4 4 8 2
1
1000
1000000
1000000000
1000000000000
```

### Sample Output 2

```
4
5
5
5
5
```
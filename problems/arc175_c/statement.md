Score: 600 points

### Problem Statement

You are given N pairs of integers (L\_1, R\_1), (L\_2, R\_2), \dots, (L\_N, R\_N). Here, L\_i \leq R\_i for all 1 \leq i \leq N.

A sequence of N integers A = (A\_1, A\_2, \ldots, A\_N) is called a **good integer sequence** if it satisfies the following condition:

* L\_i \leq A\_i \leq R\_i for all 1 \leq i \leq N.

Find the lexicographically smallest **good integer sequence** A that minimizes \displaystyle \sum\_{i = 1}^{N-1} |A\_{i+1} - A\_{i}|.

 What is lexicographical order for sequences?

A sequence S = (S\_1,S\_2,\ldots,S\_{|S|}) is said to be **lexicographically smaller** than a sequence T = (T\_1,T\_2,\ldots,T\_{|T|}) if 1. or 2. below holds.
Here, |S|, |T| denote the lengths of S and T, respectively.

1. |S| \lt |T| and (S\_1,S\_2,\ldots,S\_{|S|}) = (T\_1,T\_2,\ldots,T\_{|S|}).
2. There is an integer 1 \leq i \leq \min\lbrace |S|, |T| \rbrace such that both of the following hold:
   * (S\_1,S\_2,\ldots,S\_{i-1}) = (T\_1,T\_2,\ldots,T\_{i-1}).
   * S\_i is smaller than T\_i (as a number).

### Constraints

* All input values are integers.
* 2 \leq N \leq 5 \times 10^5
* 0 \leq L\_i \leq R\_i \leq 10^9

---

### Input

The input is given from Standard Input in the following format:

```
N
L_1 R_1
L_2 R_2
\vdots
L_N R_N
```

### Output

Print the answer in a single line in the following format:

```
A_1 A_2 \ldots A_N
```

---

### Sample Input 1

```
4
1 10
8 13
3 4
5 20
```

### Sample Output 1

```
8 8 4 5
```

(A\_1, A\_2, A\_3, A\_4) = (8, 8, 4, 5) is a good integer sequence. In this case, \sum\_{i = 1}^{N-1} |A\_{i+1} - A\_{i}| = |8 - 8| + |4 - 8| + |5 - 4| = 5, which is the minimum value of \sum\_{i = 1}^{N-1} |A\_{i+1} - A\_{i}|.

---

### Sample Input 2

```
3
20 24
3 24
1 75
```

### Sample Output 2

```
20 20 20
```

Note that when multiple good integer sequences A minimize \sum\_{i = 1}^{N-1} |A\_{i+1} - A\_{i}|, you should print the lexicographically smallest of them.

---

### Sample Input 3

```
15
335279264 849598327
446755913 822889311
526239859 548830120
181424399 715477619
342858071 625711486
448565595 480845266
467825612 647639160
160714711 449656269
336869678 545923679
61020590 573085537
626006012 816372580
135599877 389312924
511429216 547865075
561330066 605997004
539239436 921749002
```

### Sample Output 3

```
526239859 526239859 526239859 467825612 467825612 467825612 467825612 449656269 449656269 449656269 626006012 389312924 511429216 561330066 561330066
```
Score : 400 points

### Problem Statement

You are given a sequence of length N: A=(A\_1,\ldots,A\_N).

Answer Q queries given in the following format.

* You are given integers L, R, and X.
  Find the number of elements among A\_L, \ldots, A\_R whose values are equal to X.

### Constraints

* 1 \leq N \leq 2\times 10^5
* 1 \leq A\_i \leq N
* 1 \leq Q \leq 2\times 10^5
* 1\le L \leq R \leq N, 1 \leq X \leq N, for each query.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N 
A_1 A_2 \ldots A_N
Q
\mathrm{Query}_1
\mathrm{Query}_2
\vdots
\mathrm{Query}_Q
```

Here, \mathrm{Query}\_i represents the i-th query.

Each query is in the following format:

```
L R X
```

### Output

Print Q lines, the i-th of which contains the answer to the i-th query.

---

### Sample Input 1

```
5
3 1 4 1 5
4
1 5 1
2 4 3
1 5 2
1 3 3
```

### Sample Output 1

```
2
0
0
1
```

In the first query, two of (A\_1,A\_2,A\_3,A\_4,A\_5) =(3,1,4,1,5) have values equal to 1.

In the second query, zero of (A\_2,A\_3,A\_4) =(1,4,1) have values equal to 3.
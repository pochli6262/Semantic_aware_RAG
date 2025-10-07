Score: 500 points

### Problem Statement

There is an integer sequence A=(A\_1,A\_2,\ldots,A\_N) of length N, where all elements are initially set to 0. Also, there is a set S, which is initially empty.

Perform the following Q queries in order. Find the value of each element in the sequence A after processing all Q queries. The i-th query is in the following format:

* An integer x\_i is given. If the integer x\_i is contained in S, remove x\_i from S. Otherwise, insert x\_i to S. Then, for each j=1,2,\ldots,N, add |S| to A\_j if j\in S.

Here, |S| denotes the number of elements in the set S. For example, if S=\lbrace 3,4,7\rbrace, then |S|=3.

### Constraints

* 1\leq N,Q\leq 2\times10^5
* 1\leq x\_i\leq N
* All given numbers are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N Q
x_1 x_2 \ldots x_Q
```

### Output

Print the sequence A after processing all queries in the following format:

```
A_1 A_2 \ldots A_N
```

---

### Sample Input 1

```
3 4
1 3 3 2
```

### Sample Output 1

```
6 2 2
```

In the first query, 1 is inserted to S, making S=\lbrace 1\rbrace. Then, |S|=1 is added to A\_1. The sequence becomes A=(1,0,0).

In the second query, 3 is inserted to S, making S=\lbrace 1,3\rbrace. Then, |S|=2 is added to A\_1 and A\_3. The sequence becomes A=(3,0,2).

In the third query, 3 is removed from S, making S=\lbrace 1\rbrace. Then, |S|=1 is added to A\_1. The sequence becomes A=(4,0,2).

In the fourth query, 2 is inserted to S, making S=\lbrace 1,2\rbrace. Then, |S|=2 is added to A\_1 and A\_2. The sequence becomes A=(6,2,2).

Eventually, the sequence becomes A=(6,2,2).

---

### Sample Input 2

```
4 6
1 2 3 2 4 2
```

### Sample Output 2

```
15 9 12 7
```
Score : 400 points

### Problem Statement

You are given a string S consisting of `A`, `B`, `C`.

Let S^{(0)}:=S. For i=1,2,3,\ldots, let S^{(i)} be the result of simultaneously replacing the characters of S^{(i-1)} as follows: `A` → `BC`, `B` → `CA`, `C` → `AB`.

Answer Q queries. The i-th query is as follows.

* Print the k\_i-th character from the beginning of S^{(t\_i)}.

### Constraints

* S is a string of length between 1 and 10^5 (inclusive) consisting of `A`, `B`, `C`.
* 1 \leq Q \leq 10^5
* 0 \leq t\_i \leq 10^{18}
* 1 \leq k\_i \leq \min(10^{18}, the length of S^{(t\_i)})
* Q, t\_i, k\_i are integers.

---

### Input

Input is given from Standard Input in the following format:

```
S
Q
t_1 k_1
t_2 k_2
\hspace{0.4cm}\vdots
t_Q k_Q
```

### Output

Process the Q queries in ascending order of index, that is, in the given order. Each answer should be followed by a newline.

---

### Sample Input 1

```
ABC
4
0 1
1 1
1 3
1 6
```

### Sample Output 1

```
A
B
C
B
```

We have S^{(0)}=`ABC`, S^{(1)}=`BCCAAB`.

Thus, the answers to the queries are `A`, `B`, `C`, `B` in the given order.

---

### Sample Input 2

```
CBBAACCCCC
5
57530144230160008 659279164847814847
29622990657296329 861239705300265164
509705228051901259 994708708957785197
176678501072691541 655134104344481648
827291290937314275 407121144297426665
```

### Sample Output 2

```
A
A
C
A
A
```
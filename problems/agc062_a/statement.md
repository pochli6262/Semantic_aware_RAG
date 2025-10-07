Score : 400 points

### Problem Statement

For a string T=T\_1T\_2\dots T\_n of length n\ (2\leq n) consisting of `A` and `B`, we define a string f(T) of length n-1 as follows.

* Let a\_1 < a\_2 < \dots < a\_{m} be the indices i\ (1\leq i \leq n-1) such that T\_i={}`A`, and b\_1 < b\_2 < \dots < b\_k be the indices i\ (1\leq i \leq n-1) such that T\_i={}`B`. Then, let f(T)=T\_{a\_1+1}T\_{a\_2+1}\dots T\_{a\_m+1}T\_{b\_1+1}T\_{b\_2+1}\dots T\_{b\_k+1}.

For example, for the string T={}`ABBABA`, the indices i\ (1\leq i \leq 5) with T\_i={}`A` are i=1,4, and the indices i\ (1\leq i \leq 5) with T\_i={}`B` are i=2,3,5, so f(T) is T\_{1+1}T\_{4+1}T\_{2+1}T\_{3+1}T\_{5+1}={}`BBBAA`.

You are given a string S of length N consisting of `A` and `B`.

Find S after replacing S with f(S) (N-1) times.

You have T test cases to solve.

### Constraints

* 1 \leq T \leq 10^5
* 2 \leq N \leq 3 \times 10^5
* S is a string of length N consisting of `A` and `B`.
* All numbers in the input are integers.
* The sum of N over the test cases in a single input file is at most 3 \times 10^5.

---

### Input

The input is given from Standard Input in the following format:

```
T
\mathrm{case}_1
\vdots
\mathrm{case}_T
```

Each case is given in the following format:

```
N
S
```

### Output

Print T lines. The i-th line should contain the answer to the i-th test case.

---

### Sample Input 1

```
3
2
AB
3
AAA
4
ABAB
```

### Sample Output 1

```
B
A
A
```

In the first test case, S changes as `AB`{}\rightarrow {}`B`.

In the second test case, S changes as `AAA`{} \rightarrow {}`AA`{} \rightarrow {}`A`.

In the third test case, S changes as `ABAB`{}\rightarrow {}`BBA`{} \rightarrow {}`BA`{} \rightarrow {}`A`.
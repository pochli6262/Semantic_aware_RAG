Score : 500 points

### Problem Statement

There is a simple undirected graph with N vertices numbered 1 through N and M edges numbered 1 through M. Edge i connects vertex u\_i and vertex v\_i.  
Every vertex is painted either red or blue. The color of vertex i is represented by C\_i; vertex i is painted red if C\_i is 0 and blue if C\_i is 1.

Now, Takahashi is on vertex 1 and Aoki is on vertex N.  
They may repeat the following move zero or more times.

* Each of the two simultaneously moves to a vertex adjacent to the current vertex.  
  Here, the vertices that Takahashi and Aoki move to must have different colors.

By repeating the move above, can Takahashi and Aoki simultaneously end up on vertices N and 1, respectively?  
If it is possible, find the minimum number of moves required. If it is impossible, print `-1`.

You are given T at the beginning of the input. Solve the problem for T test cases.

### Constraints

* 1 \leq T \leq 1000
* 2 \leq N \leq 2000
* 1 \leq M \leq \min(\frac{N(N-1)}{2}, 2000)
* C\_i \in \lbrace 0, 1 \rbrace
* 1 \leq u\_i, v\_i \leq N
* The graph given in the input is simple.
* All values in the input are integers.
* The sum of N over all test cases does not exceed 2000.
* The sum of M over all test cases does not exceed 2000.

---

### Input

The input is given from Standard Input in the following format, where \text{test}\_i denotes the i-th test case:

```
T
\text{test}_1
\text{test}_2
\vdots
\text{test}_T
```

Each test case is given in the following format:

```
N M
C_1 C_2 \dots C_N
u_1 v_1
u_2 v_2
\vdots
u_M v_M
```

### Output

Print T lines. The i-th line should contain the answer to the i-th test case.  
For each test case, print the minimum number of moves required for Takahashi and Aoki to simultaneously end up in vertices N and 1, respectively, if it is possible, and `-1` otherwise.

---

### Sample Input 1

```
3
4 4
0 1 0 1
1 2
2 3
1 3
2 4
3 3
0 1 0
1 2
2 3
1 3
6 6
0 0 1 1 0 1
1 2
2 6
3 6
4 6
4 5
2 4
```

### Sample Output 1

```
3
-1
3
```

For the 1-st test case, Takahashi and Aoki can achieve the objective by making the following 3 moves, which is the minimum number:

* Takahashi moves to vertex 3, and Aoki moves to vertex 2.
* Takahashi moves to vertex 2, and Aoki moves to vertex 3.
* Takahashi moves to vertex 4, and Aoki moves to vertex 1.

Note that in the 1-st move, it is disallowed that both Takahashi and Aoki move to vertex 2 (because the colors of vertices that Takahashi and Aoki move to must be different.)

For the 2-nd case, no matter how they move, they cannot achieve the objective.
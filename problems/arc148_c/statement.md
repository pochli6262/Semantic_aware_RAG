Score : 500 points

### Problem Statement

We have a rooted tree with N vertices numbered 1 to N. Vertex 1 is the root, and the parent of vertex i is vertex P\_i.  
There are N coins with heads and tails, one on each vertex.  
Additionally, there are N buttons numbered 1 to N. Pressing button n flips all coins on the vertices in the subtree rooted at vertex n.

Process Q queries described below.

In the i-th query, you are given a vertex set of size M\_i: S\_i = \lbrace v\_{i,1}, v\_{i,2},\dots, v\_{i,M\_i} \rbrace.  
Now, the coins on the vertices in S\_i are facing heads-up, and the others are facing tails-up. In order to make all N coins face tails-up by repeatedly choosing a button and pressing it, at least how many button presses are needed? Print the answer, or -1 if there is no way to make all the coins face tails-up.

### Constraints

* 2 \leq N \leq 2 \times 10^5
* 1 \leq P\_i \lt i
* 1 \leq Q \leq 2 \times 10^5
* 1 \leq M\_i
* \displaystyle \sum\_{i=1}^Q M\_i \leq 2 \times 10^5
* 1 \leq v\_{i,j} \leq N
* v\_{i,1}, v\_{i,2},\dots,v\_{i,M\_i} are pairwise different.
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N Q
P_2 P_3 \dots P_N
M_1 v_{1,1} v_{1,2} \dots v_{1,M_1}
M_2 v_{2,1} v_{2,2} \dots v_{2,M_2}
\vdots
M_Q v_{Q,1} v_{Q,2} \dots v_{Q,M_Q}
```

### Output

Print Q lines. The i-th line should contain the answer to the i-th query.

---

### Sample Input 1

```
6 6
1 1 2 2 5
6 1 2 3 4 5 6
3 2 5 6
1 3
3 1 2 3
3 4 5 6
4 2 3 4 5
```

### Sample Output 1

```
1
2
1
3
2
3
```

For the first query, you can satisfy the requirement in one button press, which is the minimum needed, as follows.

* Press button 1, flipping the coins on vertices 1,2,3,4,5,6.

For the second query, you can satisfy the requirement in two button presses, which is the minimum needed, as follows.

* Press button 4, flipping the coin on vertex 4.
* Press button 2, flipping the coins on vertex 2,4,5,6.
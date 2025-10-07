Score : 600 points

### Problem Statement

We have a directed graph with N vertices and M edges. Edge i is directed from Vertex A\_i to B\_i and has a weight of C\_i.

Initially, there is a piece on Vertex v. Takahashi and Aoki will play a game where they alternate turns moving the piece as follows:

* If there is no edge that goes from the vertex on which the piece is placed, end the game.
* If there are edges that go from the vertex on which the piece is placed, choose one of those edges and move the piece along that edge.

Takahashi goes first. Takahashi tries to minimize the total weight of the edges traversed by the piece, and Aoki tries to maximize it.  
More formally, their objectives are as follows.  
Takahashi gives the first priority to ending the game in a finite number of moves. If this is possible, he tries to minimize the total weight of the edges traversed by the piece.  
Aoki gives the first priority to preventing the game from ending in a finite number of moves. If this is impossible, he tries to maximize the total weight of the edges traversed by the piece.  
(If the piece traverses the same edge multiple times, the weight is added that number of times.)

Determine whether the game ends in a finite number of moves when both players play optimally. If it ends, find the total weight of the edges traversed by the piece.

### Constraints

* 1 \leq N \leq 2\times 10^5
* 0 \leq M \leq 2\times 10^5
* 1 \leq v \leq N
* 1 \leq A\_i,B\_i \leq N
* There is no multi-edges. That is, (A\_i,B\_i)\neq(A\_j,B\_j) for i\neq j.
* There is no self-loops. That is, A\_i\neq B\_i.
* 0 \leq C\_i \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M v
A_1 B_1 C_1
A_2 B_2 C_2
\vdots
A_M B_M C_M
```

### Output

If the game does not end in a finite number of moves when both players play optimally, print `INFINITY`.  
If the game ends in a finite number of moves, print the total weight of the edges traversed by the piece.

---

### Sample Input 1

```
7 6 1
1 2 1
1 3 10
2 4 100
2 5 102
3 6 20
3 7 30
```

### Sample Output 1

```
40
```

First, Takahashi will move the piece to Vertex 3. Next, Aoki will move the piece to Vertex 7, and the game will end.  
The total weight of the edges traversed by the piece will be 10+30=40.

---

### Sample Input 2

```
3 6 3
1 2 1
2 1 2
2 3 3
3 2 4
3 1 5
1 3 6
```

### Sample Output 2

```
INFINITY
```

The game will not end in a finite number of moves.

---

### Sample Input 3

```
4 4 1
1 2 1
2 3 1
3 1 1
2 4 1
```

### Sample Output 3

```
5
```

The piece will go 1\to 2 \to 3 \to 1 \to 2\to 4.
Score : 300 points

### Problem Statement

Takahashi is a martial artist.
There are N moves that a martial artist can learn, called Move 1, 2, \ldots, N.
For each 1 \leq i \leq N, it takes T\_i minutes of practice to learn Move i.
Additionally, at the beginning of that practice, all of the Moves A\_{i,1}, A\_{i,2}, \ldots, A\_{i,K\_i} must be already learned.
Here, it is guaranteed that A\_{i,j} < i for each 1 \leq j \leq K\_i.

Takahashi has not learned any move at time 0.
He cannot practice for more than one move simultaneously, nor can he stop a practice he has already started.
Find the minimum number of minutes needed for Takahashi to learn Move N.

### Constraints

* 1 \leq N \leq 2\times 10^5
* 1 \leq T\_i \leq 10^9
* 0 \leq K\_i < i
* 1 \leq A\_{i,j} < i
* \sum\_{i=1}^N K\_i \leq 2\times 10^5
* A\_{i,1}, A\_{i,2}, \ldots, A\_{i,K\_i} are all distinct.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
T_1 K_1 A_{1,1} A_{1,2} \ldots A_{1,K_1}
T_2 K_2 A_{2,1} A_{2,2} \ldots A_{2,K_2}
\vdots
T_N K_N A_{N,1} A_{N,2} \ldots A_{N,K_N}
```

### Output

Print the minimum number of minutes needed for Takahashi to learn Move N.

---

### Sample Input 1

```
3
3 0
5 1 1
7 1 1
```

### Sample Output 1

```
10
```

Here is one possible plan for Takahashi.

* At time 0, start practicing for Move 1 to learn Move 1 at time 3.
* Then, at time 3, start practicing for Move 3 to learn Move 3 at time 10.

Here, Takahashi spends 3+7=10 minutes to learn Move 3, which is the fastest possible.
Note that he does not need to learn Move 2 to learn Move 3.

---

### Sample Input 2

```
5
1000000000 0
1000000000 0
1000000000 0
1000000000 0
1000000000 4 1 2 3 4
```

### Sample Output 2

```
5000000000
```

Note that the answer may not fit into a 32-bit integer.
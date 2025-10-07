Score : 500 points

### Problem Statement

On a number line, there are N fish swimming.

Fish i, which has a weight of W\_i, is at the coordinate X\_i at time 0 and moves at a speed of V\_i in the positive direction.

Takahashi will choose an arbitrary real number t greater than or equal to 0 and do the following action at time t just once.  
Action: Choose an arbitrary real number x. Catch all fish whose coordinates are between x and x+A, inclusive.

Find the maximum total weight of fish that he can catch.

### Constraints

* 1 \leq N \leq 2000
* 1 \leq A \leq 10^4
* 1 \leq W\_i\leq 10^4
* 0 \leq X\_i\leq 10^4
* 1 \leq V\_i\leq 10^4
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N A
W_1 X_1 V_1
W_2 X_2 V_2
\vdots
W_N X_N V_N
```

### Output

Print the answer.

---

### Sample Input 1

```
3 10
100 0 100
1 10 30
10 20 10
```

### Sample Output 1

```
111
```

At time 0.25, fish 1, 2, and 3 are at the coordinates 25, 17.5, and 22.5, respectively. Thus, the action done at this time with x=16 catches all the fish.

---

### Sample Input 2

```
3 10
100 100 100
1 10 30
10 20 10
```

### Sample Output 2

```
100
```

One optimal choice is to do the action at time 0 with x=100.

---

### Sample Input 3

```
4 10
1000 100 10
100 99 1
10 0 100
1 1 1
```

### Sample Output 3

```
1110
```

One optimal choice is to do the action at time 1 with x=100.
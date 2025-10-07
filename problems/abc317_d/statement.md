Score : 400 points

### Problem Statement

Takahashi and Aoki are competing in an election.  
There are N electoral districts. The i-th district has X\_i + Y\_i voters, of which X\_i are for Takahashi and Y\_i are for Aoki. (X\_i + Y\_i is always an odd number.)  
In each district, the majority party wins all Z\_i seats in that district. Then, whoever wins the majority of seats in the N districts as a whole wins the election. (\displaystyle \sum\_{i=1}^N Z\_i is odd.)  
At least how many voters must switch from Aoki to Takahashi for Takahashi to win the election?

### Constraints

* 1 \leq N \leq 100
* 0 \leq X\_i, Y\_i \leq 10^9
* X\_i + Y\_i is odd.
* 1 \leq Z\_i
* \displaystyle \sum\_{i=1}^N Z\_i \leq 10^5
* \displaystyle \sum\_{i=1}^N Z\_i is odd.

---

### Input

The input is given from Standard Input in the following format:

```
N
X_1 Y_1 Z_1
X_2 Y_2 Z_2
\vdots
X_N Y_N Z_N
```

### Output

Print the answer.

---

### Sample Input 1

```
1
3 8 1
```

### Sample Output 1

```
3
```

Since there is only one district, whoever wins the seat in that district wins the election.  
If three voters for Aoki in the district switch to Takahashi, there will be six voters for Takahashi and five for Aoki, and Takahashi will win the seat.

---

### Sample Input 2

```
2
3 6 2
1 8 5
```

### Sample Output 2

```
4
```

Since there are more seats in the second district than in the first district, Takahashi must win a majority in the second district to win the election.  
If four voters for Aoki in the second district switch sides, Takahashi will win five seats. In this case, Aoki will win two seats, so Takahashi will win the election.

---

### Sample Input 3

```
3
3 4 2
1 2 3
7 2 6
```

### Sample Output 3

```
0
```

If Takahashi will win the election even if zero voters switch sides, the answer is 0.

---

### Sample Input 4

```
10
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
2268 2279 16
2394 2841 18
2926 2971 20
3091 2146 20
3878 4685 38
4504 4617 29
```

### Sample Output 4

```
86
```
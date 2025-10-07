Score : 600 points

### Problem Statement

There are N people and K nations, labeled as Person 1, Person 2, \ldots, Person N and Nation 1, Nation 2, \ldots, Nation K, respectively.  
Each person belongs to exactly one nation: Person i belongs to Nation A\_i.
Additionally, there are L popular people among them: Person B\_1, Person B\_2, \ldots, Person B\_L are popular.
Initially, no two of the N people are friends.

For M pairs of people, Takahashi, a God, can make them friends by paying a certain cost: for each 1\leq i\leq M, he can pay the cost of C\_i to make Person U\_i and Person V\_i friends.

Now, for each 1\leq i\leq N, solve the following problem.

> Can Takahashi make Person i an indirect friend of a popular person belonging to a nation different from that of Person i?
> If he can do so, find the minimum total cost needed.
> Here, Person s is said to be an indirect friend of Person t when there exists a non-negative integer n and a sequence of people (u\_0, u\_1, \ldots, u\_n)
> such that u\_0=s, u\_n=t, and Person u\_i and Person u\_{i+1} are friends for each 0\leq i < n.

### Constraints

* 2 \leq N \leq 10^5
* 1 \leq M \leq 10^5
* 1 \leq K \leq 10^5
* 1 \leq L \leq N
* 1 \leq A\_i \leq K
* 1 \leq B\_1<B\_2<\cdots<B\_L\leq N
* 1\leq C\_i\leq 10^9
* 1\leq U\_i<V\_i\leq N
* (U\_i, V\_i)\neq (U\_j,V\_j) if i \neq j.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N M K L
A_1 A_2 \cdots A_N
B_1 B_2 \cdots B_L
U_1 V_1 C_1
U_2 V_2 C_2
\vdots
U_M V_M C_M
```

### Output

Let X\_i defined as follows: X\_i is -1 if it is impossible to make Person i an indirect friend of a popular person belonging to a nation different from that of Person i; otherwise, X\_i is the minimum total cost needed to do so.
Print X\_1, X\_2, \ldots, X\_N in one line, with spaces in between.

---

### Sample Input 1

```
4 4 2 2
1 1 2 2
2 3
1 2 15
2 3 30
3 4 40
1 4 10
```

### Sample Output 1

```
45 30 30 25
```

Person 1, 2, 3, 4 belong to Nation 1, 1, 2, 2, respectively, and there are two popular people: Person 2 and 3. Here,

* For Person 1, the only popular person belonging to a different nation is Person 3. To make them indirect friends with the minimum cost, we should pay the cost of 15 to make Person 1 and 2 friends and pay 30 to make Person 2 and 3 friends, for a total of 15+30=45.
* For Person 2, the only popular person belonging to a different nation is Person 3. The minimum cost is achieved by making Person 2 and 3 friends by paying 30.
* For Person 3, the only popular person belonging to a different nation is Person 2. The minimum cost is achieved by making Person 2 and 3 friends by paying 30.
* For Person 4, the only popular person belonging to a different nation is Person 2. To make them indirect friends with the minimum cost, we should pay the cost of 15 to make Person 1 and 2 friends and pay 10 to make Person 1 and 4 friends, for a total of 15+10=25.

---

### Sample Input 2

```
3 1 3 1
1 2 3
1
1 2 1000000000
```

### Sample Output 2

```
-1 1000000000 -1
```

Note that, for Person 1, Person 1 itself is indeed an indirect friend, but it does not belong to a different nation, so there is no popular person belonging to a different nation.
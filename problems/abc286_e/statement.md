Score : 500 points

### Problem Statement

There are N cities. There are also one-way direct flights that connect different cities.  
The availability of direct flights is represented by N strings S\_1,S\_2,\ldots,S\_N of length N each.
If the j-th character of S\_i is `Y`, there is a direct flight from city i to city j;
if it is `N`, there is not.  
Each city sells a souvenir; city i sells a souvenir of value A\_i.

Consider the following problem:

> Takahashi is currently at city S and wants to get to city T (that is different from city S) using some direct flights.  
> Every time he visits a city (including S and T), he buys a souvenir there.  
> If there are multiple routes from city S to city T, Takahashi decides the route as follows:
>
> * He tries to minimize the number of direct flights in the route from city S to city T.
> * Then he tries to maximize the total value of the souvenirs he buys.
>
> Determine if he can travel from city S to city T using the direct flights.
> If he can, find the "number of direct flights" and "total value of souvenirs" in the route that satisfies the conditions above.

You are given Q pairs (U\_i,V\_i) of distinct cities.  
For each 1\leq i\leq Q, print the answer to the problem above when S=U\_i and T=V\_i.

### Constraints

* 2 \leq N \leq 300
* 1\leq A\_i\leq 10^9
* S\_i is a string of length N consisting of `Y` and `N`.
* The i-th character of S\_i is `N`.
* 1\leq Q\leq N(N-1)
* 1\leq U\_i,V\_i\leq N
* U\_i\neq V\_i
* If i \neq j, then (U\_i,V\_i)\neq (U\_j,V\_J).
* N,A\_i,Q,U\_i, and V\_i are all integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 \ldots A_N
S_1
S_2
\vdots
S_N
Q
U_1 V_1
U_2 V_2
\vdots
U_Q V_Q
```

### Output

Print Q lines.  
The i-th (1\leq i\leq Q) line should contain
`Impossible` if he cannot travel from city U\_i to city V\_i;
if he can, the line should contain "the number of direct flights" and "the total value of souvenirs" in the route chosen as described above, in this order, separated by a space.

---

### Sample Input 1

```
5
30 50 70 20 60
NYYNN
NNYNN
NNNYY
YNNNN
YNNNN
3
1 3
3 1
4 5
```

### Sample Output 1

```
1 100
2 160
3 180
```

For (S,T)=(U\_1,V\_1)=(1,3), there is a direct flight from city 1 to city 3,
so the minimum possible number of direct flights is 1, which is achieved when he uses that direct flight.
In this case, the total value of the souvenirs is A\_1+A\_3=30+70=100.

For (S,T)=(U\_2,V\_2)=(3,1), the minimum possible number of direct flights is 2.
The following two routes achieve the minimum: cities 3\to 4\to 1, and cities 3\to 5\to 1.
Since the total value of souvenirs in the two routes are 70+20+30=120 and 70+60+30=160, respectively,
so he chooses the latter route, and the total value of the souvenirs is 160.

For (S,T)=(U\_3,V\_3)=(4,5), the number of direct flights is minimum when he travels cities 4\to 1\to 3\to 5, where the total value of the souvenirs is 20+30+70+60=180.

---

### Sample Input 2

```
2
100 100
NN
NN
1
1 2
```

### Sample Output 2

```
Impossible
```

There may be no direct flight at all.
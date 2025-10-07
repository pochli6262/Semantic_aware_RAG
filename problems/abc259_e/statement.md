Score : 500 points

### Problem Statement

There are N integers a\_1,\ldots,a\_N written on a whiteboard.  
Here, a\_i can be represented as a\_i = p\_{i,1}^{e\_{i,1}} \times \ldots \times p\_{i,m\_i}^{e\_{i,m\_i}} using m\_i prime numbers p\_{i,1} \lt \ldots \lt p\_{i,m\_i} and positive integers e\_{i,1},\ldots,e\_{i,m\_i}.  
You will choose one of the N integers to replace it with 1.  
Find the number of values that can be the least common multiple of the N integers after the replacement.

### Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq m\_i
* \sum{m\_i} \leq 2 \times 10^5
* 2 \leq p\_{i,1} \lt \ldots \lt p\_{i,m\_i} \leq 10^9
* p\_{i,j} is prime.
* 1 \leq e\_{i,j} \leq 10^9
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
N
m_1
p_{1,1} e_{1,1}
\vdots
p_{1,m_1} e_{1,m_1}
m_2
p_{2,1} e_{2,1}
\vdots
p_{2,m_2} e_{2,m_2}
\vdots
m_N
p_{N,1} e_{N,1}
\vdots
p_{N,m_N} e_{N,m_N}
```

### Output

Print the answer.

---

### Sample Input 1

```
4
1
7 2
2
2 2
5 1
1
5 1
2
2 1
7 1
```

### Sample Output 1

```
3
```

The integers on the whiteboard are a\_1 =7^2=49, a\_2=2^2 \times 5^1 = 20, a\_3 = 5^1 = 5, a\_4=2^1 \times 7^1 = 14.  
If you replace a\_1 with 1, the integers on the whiteboard become 1,20,5,14, whose least common multiple is 140.  
If you replace a\_2 with 1, the integers on the whiteboard become 49,1,5,14, whose least common multiple is 490.  
If you replace a\_3 with 1, the integers on the whiteboard become 49,20,1,14, whose least common multiple is 980.  
If you replace a\_4 with 1, the integers on the whiteboard become 49,20,5,1, whose least common multiple is 980.  
Therefore, the least common multiple of the N integers after the replacement can be 140, 490, or 980, so the answer is 3.

---

### Sample Input 2

```
1
1
998244353 1000000000
```

### Sample Output 2

```
1
```

There may be enormous integers on the whiteboard.
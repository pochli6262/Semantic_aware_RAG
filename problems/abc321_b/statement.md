Score : 200 points

### Problem Statement

There is an exam structured as follows.

* The exam consists of N rounds called round 1 to N.
* In each round, you are given an integer score between 0 and 100, inclusive.
* Your final grade is the sum of the N-2 of the scores earned in the rounds excluding the highest and lowest.
  + Formally, let S=(S\_1,S\_2,\dots,S\_N) be the sequence of the scores earned in the rounds sorted in ascending order, then the final grade is S\_2+S\_3+\dots+S\_{N-1}.

Now, N-1 rounds of the exam have ended, and your score in round i was A\_i.  
Print the minimum score you must earn in round N for a final grade of X or higher.  
If your final grade will never be X or higher no matter what score you earn in round N, print `-1` instead.  
Note that your score in round N can only be an integer between 0 and 100.

### Constraints

* All input values are integers.
* 3 \le N \le 100
* 0 \le X \le 100 \times (N-2)
* 0 \le A\_i \le 100

---

### Input

The input is given from Standard Input in the following format:

```
N X
A_1 A_2 \dots A_{N-1}
```

### Output

Print the answer.

---

### Sample Input 1

```
5 180
40 60 80 50
```

### Sample Output 1

```
70
```

Your scores in the first four rounds were 40, 60, 80, and 50.  
If you earn a score of 70 in round 5, the sequence of the scores sorted in ascending order will be S=(40,50,60,70,80), for a final grade of 50+60+70=180.  
It can be shown that 70 is the minimum score you must earn for a final grade of 180 or higher.

---

### Sample Input 2

```
3 100
100 100
```

### Sample Output 2

```
0
```

Your scores in the first two rounds were 100 and 100.  
If you earn a score of 0 in round 3, the sequence of the scores sorted in ascending order will be S=(0,100,100), for a final grade of 100.  
Note that the highest score, 100, is earned multiple times, and only one of them is excluded. (The same goes for the lowest score.)  
It can be shown that 0 is the minimum score you must earn for a final grade of 100 or higher.

---

### Sample Input 3

```
5 200
0 0 99 99
```

### Sample Output 3

```
-1
```

Your scores in the first four rounds were 0, 0, 99, and 99.  
It can be shown that your final grade will never be 200 or higher no matter what score you earn in round 5.

---

### Sample Input 4

```
10 480
59 98 88 54 70 24 8 94 46
```

### Sample Output 4

```
45
```
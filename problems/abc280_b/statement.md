Score : 200 points

### Problem Statement

You are given an integer N and a sequence S=(S\_1,\ldots,S\_N) of length N.

Find a sequence A=(A\_1,\ldots,A\_N) of length N that satisfies the following condition for all k=1,\ldots,N:

* A\_1+A\_2+\ldots+A\_k = S\_k.

Such a sequence A always exists and is unique.

### Constraints

* 1 \leq N \leq 10
* -10^9\leq S\_i \leq 10^9
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N
S_1 \ldots S_N
```

### Output

Print the elements of a sequence A=(A\_1,\ldots,A\_N) that satisfies all the conditions in order, separated by spaces.

---

### Sample Input 1

```
3
3 4 8
```

### Sample Output 1

```
3 1 4
```

The sequence in the output actually satisfies all the conditions:

* A\_1=3=S\_1;
* A\_1+A\_2=3+1=4=S\_2;
* A\_1+A\_2+A\_3=3+1+4=8=S\_3.

---

### Sample Input 2

```
10
314159265 358979323 846264338 -327950288 419716939 -937510582 97494459 230781640 628620899 -862803482
```

### Sample Output 2

```
314159265 44820058 487285015 -1174214626 747667227 -1357227521 1035005041 133287181 397839259 -1491424381
```
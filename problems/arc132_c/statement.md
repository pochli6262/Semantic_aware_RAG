Score : 600 points

### Problem Statement

Given is a sequence a\_1,\dots,a\_n consisting of 1,\dots, n and -1, along with an integer d.
How many sequences p\_1,\dots,p\_n satisfy the conditions below?
Print the count modulo 998244353.

* p\_1,\dots,p\_n is a permutation of 1,\dots, n.
* For each i=1,\dots,n, a\_i=p\_i if a\_i\neq -1. (That is, p\_1,\dots,p\_n can be obtained by replacing the -1s in a\_1,\dots,a\_n in some way.)
* For each i=1,\dots,n, |p\_i - i|\le d.

### Constraints

* 1 \le d \le 5
* d < n \le 500
* 1\le a\_i \le n or a\_i=-1.
* |a\_i-i|\le d if a\_i\neq -1.
* a\_i\neq a\_j, if i\neq j and a\_i, a\_j \neq -1.
* All values in input are integers.

---

### Input

Input is given from Standard Input in the following format:

```
n d
a_1 \dots a_n
```

### Output

Print the number of sequences that satisfy the conditions, modulo 998244353.

---

### Sample Input 1

```
4 2
3 -1 1 -1
```

### Sample Output 1

```
2
```

The conditions are satisfied by (3,2,1,4) and (3,4,1,2).

---

### Sample Input 2

```
5 1
2 3 4 5 -1
```

### Sample Output 2

```
0
```

The only permutation of 1,2,3,4,5 that can be obtained by replacing the -1 is (2,3,4,5,1), whose fifth term violates the condition, so the answer is 0.

---

### Sample Input 3

```
16 5
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

### Sample Output 3

```
794673086
```

Print the count modulo 998244353.
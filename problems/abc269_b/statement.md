Score : 200 points

### Problem Statement

Takahashi generated 10 strings S\_1,S\_2,\dots,S\_{10} as follows.

* First, let S\_i (1 \le i \le 10)= `..........` (10 `.`s in a row).
* Next, choose four integers A, B, C, and D satisfying all of the following.
  + 1 \le A \le B \le 10.
  + 1 \le C \le D \le 10.
* Then, for every pair of integers (i,j) satisfying all of the following, replace the j-th character of S\_i with `#`.
  + A \le i \le B.
  + C \le j \le D.

You are given S\_1,S\_2,\dots,S\_{10} generated as above. Find the integers A, B, C, and D Takahashi chose.  
It can be proved that such integers A, B, C, and D uniquely exist (there is just one answer) under the Constraints.

### Constraints

* S\_1,S\_2,\dots,S\_{10} are strings, each of length 10, that can be generated according to the Problem Statement.

---

### Input

The input is given from Standard Input in the following format:

```
S_1
S_2
\vdots
S_{10}
```

### Output

Print the answer in the following format:

```
A B
C D
```

---

### Sample Input 1

```
..........
..........
..........
..........
...######.
...######.
...######.
...######.
..........
..........
```

### Sample Output 1

```
5 8
4 9
```

Here, Takahashi chose A=5, B=8, C=4, D=9.  
This choice generates 10 strings S\_1,S\_2,\dots,S\_{10}, each of length 10, where the 4-th through 9-th characters of S\_5,S\_6,S\_7,S\_8 are `#`, and the other characters are `.`.  
These are equal to the strings given in the input.

---

### Sample Input 2

```
..........
..#.......
..........
..........
..........
..........
..........
..........
..........
..........
```

### Sample Output 2

```
2 2
3 3
```

---

### Sample Input 3

```
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
```

### Sample Output 3

```
1 10
1 10
```
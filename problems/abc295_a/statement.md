Score : 100 points

### Problem Statement

You are given N strings W\_1,W\_2,\dots,W\_N consisting of lowercase English letters.  
If one or more of these strings equal `and`, `not`, `that`, `the`, or `you`, then print `Yes`; otherwise, print `No`.

### Constraints

* N is an integer between 1 and 100, inclusive.
* 1 \le |W\_i| \le 50 (|W\_i| is the length of W\_i.)
* W\_i consists of lowercase English letters.

---

### Input

The input is given from Standard Input in the following format:

```
N
W_1 W_2 \dots W_N
```

### Output

Print the answer.

---

### Sample Input 1

```
10
in that case you should print yes and not no
```

### Sample Output 1

```
Yes
```

We have, for instance, W\_4= `you`, so you should print `Yes`.

---

### Sample Input 2

```
10
in diesem fall sollten sie no und nicht yes ausgeben
```

### Sample Output 2

```
No
```

None of the strings W\_i equals any of `and`, `not`, `that`, `the`, and `you`.
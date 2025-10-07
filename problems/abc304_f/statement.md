Score : 525 points

### Problem Statement

Takahashi and Aoki will work part-time for the next N days.  
Takahashi's shift schedule is given by the string S, where the i-th character of S is `#` if he works on the i-th day, and `.` if he is absent on the i-th day.  
Based on this, Aoki created his shift schedule as follows.

* First, take a positive divisor M of N that is not equal to N.
* Next, decide the attendance for the first M days.
* Finally, for i = 1, 2, \ldots, N - M in this order, decide the attendance for the (M + i)-th day so that it matches the attendance for the i-th day.

Note that different values of M may lead to the same final shift schedule.

Find the number of possible shift schedules for Aoki such that at least one of Takahashi and Aoki works on each of the N days, modulo 998244353.

### Constraints

* N is an integer between 2 and 10^5, inclusive.
* S is a string of length N consisting of `#` and `.`.

---

### Input

The input is given from Standard Input in the following format:

```
N
S
```

### Output

Print the answer.

---

### Sample Input 1

```
6
##.#.#
```

### Sample Output 1

```
3
```

Takahashi works on days 1, 2, 4, and 6.  
Let T be the string representing Aoki's shift schedule, where the i-th character of T is `#` if he works on the i-th day, and `.` if he is absent on the i-th day.  
There are three possible strings for T: `######`, `#.#.#.`, and `.##.##`.

The first shift schedule can be realized by choosing M = 1 or 2 or 3, the second by choosing M = 2, and the third by choosing M = 3.

---

### Sample Input 2

```
7
...####
```

### Sample Output 2

```
1
```

---

### Sample Input 3

```
12
####.####.##
```

### Sample Output 3

```
19
```
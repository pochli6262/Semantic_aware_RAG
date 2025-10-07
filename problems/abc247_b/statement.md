Score : 200 points

### Problem Statement

There are N people numbered Person 1, Person 2, \dots, and Person N. Person i has a family name s\_i and a given name t\_i.

Consider giving a nickname to each of the N people. Person i's nickname a\_i should satisfy all the conditions below.

* a\_i coincides with Person i's family name or given name. In other words, a\_i = s\_i and/or a\_i = t\_i holds.
* a\_i does not coincide with the family name and the given name of any other person. In other words, for all integer j such that 1 \leq j \leq N and i \neq j, it holds that a\_i \neq s\_j and a\_i \neq t\_j.

Is it possible to give nicknames to all the N people? If it is possible, print `Yes`; otherwise, print `No`.

### Constraints

* 2 \leq N \leq 100
* N is an integer.
* s\_i and t\_i are strings of lengths between 1 and 10 (inclusive) consisting of lowercase English alphabets.

---

### Input

Input is given from Standard Input in the following format:

```
N
s_1 t_1
s_2 t_2
\vdots
s_N t_N
```

### Output

If it is possible to give nicknames to all the N people, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
3
tanaka taro
tanaka jiro
suzuki hanako
```

### Sample Output 1

```
Yes
```

The following assignment satisfies the conditions of nicknames described in the Problem Statement: a\_1 = `taro`, a\_2 = `jiro`, a\_3 = `hanako`. (a\_3 may be `suzuki`, too.)  
However, note that we cannot let a\_1 = `tanaka`, which violates the second condition of nicknames, since Person 2's family name s\_2 is `tanaka` too.

---

### Sample Input 2

```
3
aaa bbb
xxx aaa
bbb yyy
```

### Sample Output 2

```
No
```

There is no way to give nicknames satisfying the conditions in the Problem Statement.

---

### Sample Input 3

```
2
tanaka taro
tanaka taro
```

### Sample Output 3

```
No
```

There may be a pair of people with the same family name and the same given name.

---

### Sample Input 4

```
3
takahashi chokudai
aoki kensho
snu ke
```

### Sample Output 4

```
Yes
```

We can let a\_1 = `chokudai`, a\_2 = `kensho`, and a\_3 = `ke`.
Score : 100 points

### Problem Statement

Naohiro has a monster. The monster's current health is H.  
He also has N kinds of potions, numbered from 1 to N in ascending order of effectiveness.  
If you give the monster potion n, its health will increase by P\_n. Here, P\_1 \lt P\_2 \lt \dots \lt P\_N.

He wants to increase the monster's health to X or above by giving it one of the potions.  
Print the number of the least effective potion that can achieve the purpose. (The constraints guarantee that such a potion exists.)

### Constraints

* 2 \leq N \leq 100
* 1 \leq H \lt X \leq 999
* 1 \leq P\_1 \lt P\_2 \lt \dots \lt P\_N = 999
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N H X
P_1 P_2 \dots P_N
```

### Output

Print the number of the least effective potion that can achieve the purpose.

---

### Sample Input 1

```
3 100 200
50 200 999
```

### Sample Output 1

```
2
```

Below is the change in the monster's health when one of the potions is given to the monster.

* If potion 1 is given, the monster's health becomes 100 + 50 = 150.
* If potion 2 is given, the monster's health becomes 100 + 200 = 300.
* If potion 3 is given, the monster's health becomes 100 + 999 = 1099.

The potions that increase the monster's health to at least X = 200 are potions 2 and 3.
The answer is the least effective of them, which is potion 2.

---

### Sample Input 2

```
2 10 21
10 999
```

### Sample Output 2

```
2
```

---

### Sample Input 3

```
10 500 999
38 420 490 585 613 614 760 926 945 999
```

### Sample Output 3

```
4
```
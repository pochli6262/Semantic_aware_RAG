Score: 600 points

### Problem Statement

This year's AtCoder mayoral election has two candidates, A and B, and N voters have cast their votes. The voters are assigned numbers from 1 to N, and voter i (1 \leq i \leq N) voted for candidate c\_i.

Now, the votes will be counted. As each vote is counted, the provisional result will be announced as one of the following three outcomes:

* **Result A:** Currently, candidate A has more votes.
* **Result B:** Currently, candidate B has more votes.
* **Result C:** Currently, candidates A and B have the same number of votes.

There is a rule regarding the order of vote counting: votes from all voters except voter 1 must be counted in ascending order of their voter numbers. (The vote from voter 1 may be counted at any time.)

How many different sequences of provisional results could be announced?

What is a sequence of provisional results?Let s\_i be the result (`A`, `B`, or `C`) reported when the i-th vote (1 \leq i \leq N) is counted. The sequence of provisional results refers to the string s\_1 s\_2 \dots s\_N.

### Constraints

* N is an integer such that 2 \leq N \leq 1000000.
* Each of c\_1, c\_2, \dots, c\_N is `A` or `B`.

---

### Input

The input is given from Standard Input in the following format:

```
N
c_1 c_2 \cdots c_N
```

### Output

Print the answer.

---

### Sample Input 1

```
4
AABB
```

### Sample Output 1

```
3
```

In this sample input, there are four possible orders in which the votes may be counted:

* The votes are counted in the order of voter 1 \to 2 \to 3 \to 4.
* The votes are counted in the order of voter 2 \to 1 \to 3 \to 4.
* The votes are counted in the order of voter 2 \to 3 \to 1 \to 4.
* The votes are counted in the order of voter 2 \to 3 \to 4 \to 1.

The sequences of preliminary results for these will be `AAAC`, `AAAC`, `ACAC`, `ACBC` from top to bottom, so there are three possible sequences of preliminary results.

---

### Sample Input 2

```
4
AAAA
```

### Sample Output 2

```
1
```

No matter the order of counting, the sequence of preliminary results will be `AAAA`.

---

### Sample Input 3

```
10
BBBAAABBAA
```

### Sample Output 3

```
5
```

---

### Sample Input 4

```
172
AABAAAAAABBABAABBBBAABBAAABBABBABABABBAAABAAABAABAABBBBABBBABBABBBBBBBBAAABAAABAAABABBBAABAAAABABBABBABBBBBABAABAABBBABABBAAAABAABABBBABAAAABBBBABBBABBBABAABBBAAAABAAABAAAB
```

### Sample Output 4

```
24
```
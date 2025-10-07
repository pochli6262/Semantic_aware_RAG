Score : 600 points

### Problem Statement

We have a string S consisting of lowercase English letters.  
Bob just thinks about palindromes every day. He decided to choose some of the substrings of S that are palindromes and tell them to Anna.

Anna gets angry if one of the palindromes told by Bob is a substring of another.

How many palindromes can Bob choose while not making Anna angry?

### Notes

A **substring** of S is the result of deleting zero or more characters from the beginning and the end of S.  
For example, `ab` is a substring of `abc`, while `ac` is not a substring of `abc`.

### Constraints

* 1 \leq |S| \leq 200
* S consists of lowercase English letters.

---

### Input

Input is given from Standard Input in the following format:

```
S
```

### Output

Print the answer.

---

### Sample Input 1

```
ababb
```

### Sample Output 1

```
3
```

Three palindromes `aba`, `bab`, `bb` can be chosen.

---

### Sample Input 2

```
xyz
```

### Sample Output 2

```
3
```

Three palindromes `x`, `y`, `z` can be chosen.

---

### Sample Input 3

```
xxxxxxxxxx
```

### Sample Output 3

```
1
```
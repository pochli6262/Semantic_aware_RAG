Scoring: 100 points

### Problem Statement

You are given a string S consisting of `<`, `=`, and `>`.  
Determine whether S is a **bidirectional arrow** string.  
A string S is a bidirectional arrow string if and only if there is a positive integer k such that S is a concatenation of one `<`, k `=`s, and one `>`, in this order, with a length of (k+2).

### Constraints

* S is a string of length between 3 and 100, inclusive, consisting of `<`, `=`, and `>`.

---

### Input

The input is given from Standard Input in the following format:

```
S
```

### Output

If S is a **bidirectional arrow** string, print `Yes`; otherwise, print `No`.

---

### Sample Input 1

```
<====>
```

### Sample Output 1

```
Yes
```

`<====>` is a concatenation of one `<`, four `=`s, and one `>`, in this order, so it is a bidirectional arrow string.  
Hence, print `Yes`.

---

### Sample Input 2

```
==>
```

### Sample Output 2

```
No
```

`==>` does not meet the condition for a bidirectional arrow string.  
Hence, print `No`.

---

### Sample Input 3

```
<>>
```

### Sample Output 3

```
No
```
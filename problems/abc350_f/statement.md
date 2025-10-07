Score: 550 points

### Problem Statement

You are given a string S = S\_1 S\_2 S\_3 \dots S\_{|S|} consisting of uppercase and lowercase English letters, `(`, and `)`.  
The parentheses in the string S are properly matched.

Repeat the following operation until no more operations can be performed:

* First, select one pair of integers (l, r) that satisfies all of the following conditions:
  + l < r
  + S\_l = `(`
  + S\_r = `)`
  + Each of the characters S\_{l+1}, S\_{l+2}, \dots, S\_{r-1} is an uppercase or lowercase English letter.
* Let T = \overline{S\_{r-1} S\_{r-2} \dots S\_{l+1}}.
  + Here, \overline{x} denotes the string obtained by toggling the case of each character in x (uppercase to lowercase and vice versa).
* Then, delete the l-th through r-th characters of S and insert T at the position where the deletion occurred.

Refer to the sample inputs and outputs for clarification.

It can be proved that it is possible to remove all `(`s and `)`s from the string using the above operations, and the final string is independent of how and in what order the operations are performed.  
Determine the final string.

What does it mean that the parentheses in S are properly matched?
First, a correct parenthesis sequence is defined as follows:

* A correct parenthesis sequence is a string that satisfies one of the following conditions:

+ It is an empty string.
+ There exists a correct parenthesis sequence A, and the string is formed by concatenating `(`, A, `)` in this order.
+ There exist non-empty correct parenthesis sequences A and B, and the string is formed by concatenating A and B in this order.

The parentheses in S are properly matched if and only if the `(`s and `)`s extracted from S without changing the order form a correct parenthesis sequence.

### Constraints

* 1 \le |S| \le 5 \times 10^5
* S consists of uppercase and lowercase English letters, `(`, and `)`.
* The parentheses in S are properly matched.

---

### Input

The input is given from Standard Input in the following format:

```
S
```

### Output

Print the final string.

---

### Sample Input 1

```
((A)y)x
```

### Sample Output 1

```
YAx
```

Let us perform the operations for S = `((A)y)x`.

* Choose l=2 and r=4. The substring `(A)` is removed and replaced with `a`.
  + After this operation, S = `(ay)x`.
* Choose l=1 and r=4. The substring `(ay)` is removed and replaced with `YA`.
  + After this operation, S = `YAx`.

After removing the parentheses, the string becomes `YAx`, which should be printed.

---

### Sample Input 2

```
((XYZ)n(X(y)Z))
```

### Sample Output 2

```
XYZNXYZ
```

Let us perform the operations for S = `((XYZ)n(X(y)Z))`.

* Choose l=10 and r=12. The substring `(y)` is removed and replaced with `Y`.
  + After this operation, S = `((XYZ)n(XYZ))`.
* Choose l=2 and r=6. The substring `(XYZ)` is removed and replaced with `zyx`.
  + After this operation, S = `(zyxn(XYZ))`.
* Choose l=6 and r=10. The substring `(XYZ)` is removed and replaced with `zyx`.
  + After this operation, S = `(zyxnzyx)`.
* Choose l=1 and r=9. The substring `(zyxnzyx)` is removed and replaced with `XYZNXYZ`.
  + After this operation, S = `XYZNXYZ`.

After removing the parentheses, the string becomes `XYZNXYZ`, which should be printed.

---

### Sample Input 3

```
(((()))(()))(())
```

### Sample Output 3

```

```

The final outcome may be an empty string.

---

### Sample Input 4

```
dF(qT(plC())NnnfR(GsdccC))PO()KjsiI((ysA)eWW)ve
```

### Sample Output 4

```
dFGsdccCrFNNnplCtQPOKjsiIwwEysAve
```
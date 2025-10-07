Score : 700 points

### Problem Statement

PCT has a permutation (P\_1,P\_2,\dots,P\_N) of (1,2,\dots,N). You are only informed of N.

You can ask him at most 25000 questions of the following form.

* Specify a triple of integers (i,j,k) such that 1 \le i,j,k \le N and ask whether P\_i + P\_j > P\_k.

Find all of P\_1,P\_2,\dots,P\_N.

### Constraints

* 1 \le N \le 2000
* P is decided before the start of the interaction of your program and the judge.

### Input and Output

**This is an interactive task**, where your program and the judge interact via input and output.

First, your program is given N, the length of the permutation, from Standard Input:

```
N
```

Then, you get to ask questions.
Print your question to Standard Output in the following format: (There should be a newline at the end.)

```
? i j k
```

If the question is valid, the answer ans will be given from Standard Input:

```
ans
```

Here, ans is `Yes` or `No`.

If the question is malformed or judged invalid because you have asked more questions than allowed, `-1` will be given from Standard Input:

```
-1
```

Here, the submission has already been judged incorrect. The judge will end the interaction at this point; preferably, your program should also quit.

Once you have identified all of P\_1, P\_2, \dots, P\_N, print them to Standard Output in the following format: (There should be a newline at the end.)

```
! P_1 P_2 \dots P_N
```

### Judging

* **Each time you print something, end it with a newline and flush Standard Output. Otherwise, you might get a TLE verdict.**
* After printing the answer (or receiving `-1`), immediately terminate the program normally. Otherwise, the verdict will be indeterminate.
* Note that unnecessary newlines will be considered as malformed output.

### Sample Interaction

Below is an interaction with N = 4 and P=(3,1,2,4).

| Input | Output | Description |
| --- | --- | --- |
| `4` |  | N is given. |
|  | `?` `1` `2` `3` | As the first question, you ask whether P\_1 + P\_2 > P\_3. |
| `Yes` |  | We have P\_1 + P\_2=4 and P\_3=2, so the answer is `Yes`. |
||  |  |  |
| --- | --- | --- |
|  | `?` `2` `3` `3` | As the second question, you ask whether P\_2 + P\_3 > P\_3. |
| `Yes` |  | We have P\_2 + P\_3=3 and P\_3=2, so the answer is `Yes`. |
||  |  |  |
| --- | --- | --- |
|  | `?` `2` `3` `4` | As the third question, you ask whether P\_2 + P\_3 > P\_4. |
| `No` |  | We have P\_2 + P\_3=3 and P\_4=4, so the answer is `No`. |
||  |  |  |
| --- | --- | --- |
|  | `!` `3` `1` `2` `4` | You print P\_1,P\_2,P\_3,P\_4. We do have P=(3,1,2,4), so you get an AC. |
|
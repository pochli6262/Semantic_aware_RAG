Score : 400 points

### Problem Statement

This is an **interactive task**, where your program and the judge interact via Standard Input and Output.

The judge has a string of length N consisting of 0 and 1: S = S\_1S\_2\ldots S\_N.
Here, S\_1 = 0 and S\_N = 1.

You are given the length N of S, but not the contents of S.
Instead, you can ask the judge at most 20 questions as follows.

* Choose an integer i such that 1 \leq i \leq N and ask the value of S\_i.

Print an integer p such that 1 \leq p \leq N-1 and S\_p \neq S\_{p+1}.  
It can be shown that such p always exists under the settings of this problem.

### Constraints

* 2 \leq N \leq 2 \times 10^5

### Input and Output

First, receive the length N of the string S from Standard Input:

```
N
```

Then, you get to ask the judge at most 20 questions as described in the problem statement.

Print each question to Standard Output in the following format, where i is an integer satisfying 1 \leq i \leq N:

```
? i
```

In response to this, the value of S\_i will be given from Standard Input in the following format:

```
S_i
```

Here, S\_i is 0 or 1.

When you find an integer p satisfying the condition in the problem statement, print it in the following format, and immediately quit the program:

```
! p
```

If multiple solutions exist, you may print any of them.

### Notes

* **Print a newline and flush Standard Output at the end of each message. Otherwise, you may get a TLE verdict.**
* **If there is malformed output during the interaction or your program quits prematurely, the verdict will be indeterminate.**
* After printing the answer, immediately quit the program. Otherwise, the verdict will be indeterminate.
* The string S will be fixed at the start of the interaction and will not be changed according to your questions or other factors.

---

### Sample Input and Output

In the following interaction, N = 7 and S = 0010011.

| Input | Output | Description |
| --- | --- | --- |
| `7` |  | N is given. |
|  | `? 1` | Ask the value of S\_1. |
||  |  |  |
| --- | --- | --- |
| `0` |  | The judge responds with S\_1 = 0. |
|  | `? 6` | Ask the value of S\_6. |
||  |  |  |
| --- | --- | --- |
| `1` |  | The judge responds with S\_6 = 1. |
|  | `? 5` | Ask the value of S\_5. |
||  |  |  |
| --- | --- | --- |
| `0` |  | The judge responds with S\_5 = 0. |
|  | `! 5` | Present p = 5 as an integer satisfying the condition. |
|

For the presented p = 5, we have 1 \leq p \leq N-1 and S\_p \neq S\_{p+1}.
Thus, if the program immediately quits here, this case will be judged as correctly solved.
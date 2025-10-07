Score : 550 points

### Problem Statement

This is an **interactive task** (where your program and the judge interact via Standard Input and Output).

You are given an integer N and an **odd number** K.  
The judge has a hidden length-N sequence A = (A\_1, A\_2, \dots, A\_N) consisting of 0 and 1.

While you cannot directly access the elements of sequence A,
you are allowed to ask the judge the following query at most N times.

* Choose distinct integers x\_1, x\_2, \dots, and x\_K between 1 and N, inclusive, to ask the parity of A\_{x\_1} + A\_{x\_2} + \dots + A\_{x\_K}.

Determine (A\_1, A\_2, \dots, A\_N) by at most N queries, and print the answer.  
Here, **the judge is adaptive**. In other words, the judge may modify the contents of A as long as it is consistent with the responses to the past queries.  
Therefore, your program is considered correct if the output satisfies the following condition, and incorrect otherwise:

* your program prints a sequence consistent with the responses to the queries so far, and that is the only such sequence.

### Constraints

* 1 \leq K \lt N \leq 1000
* K is odd.
* A\_i is 0 or 1.

### Input and Output

This is an **interactive task** (where your program and the judge interact via Standard Input and Output).

First of all, receive N and K from Standard Input.

```
N K
```

Then, repeat asking queries until you can uniquely determine (A\_1, A\_2, \dots, A\_N).  
Each query should be printed to Standard Output in the following format, where x\_1, x\_2, \dots, and x\_K are K distinct integers between 1 and N, inclusive.

```
? x_1 x_2 \dots x_K
```

The response to the query is given from Standard Input in the following format.

```
T
```

Here, T denotes the response to the query.

* T is `0` when A\_{x\_1} + A\_{x\_2} + \dots + A\_{x\_K} is even, and
* T is `1` when A\_{x\_1} + A\_{x\_2} + \dots + A\_{x\_K} is odd.

However, if x\_1, x\_2, \dots and x\_K do not satisfy the constraints, or the number of queries exceeds N, then T is `-1`.

If the judge returns `-1`, your program is already considered incorrect, so terminate the program immediately.

When you can determine all the elements of A, print those elements in the following format, and terminate the program immediately.

```
! A_1 A_2 \dots A_N
```

### Notes

* **Print a newline and flush Standard Output at the end of each message. Otherwise, you may get a TLE verdict.**
* **The verdict will be indeterminate if there is malformed output during the interaction or your program quits prematurely.**
* Terminate the program immediately after printing the answer, or the verdict will be indeterminate.
* The judge for this problem is adaptive. This means that the judge may modify the contents of A as long as it is consistent with the responses to the past queries.

### Sample Interaction

In the following interaction, N=5 and K=3. **Note that the following output itself will result in WA.**  
Here, A = (1, 0, 1, 1, 0) is indeed consistent with the responses, but so is (0, 0, 1, 0, 0), so sequence A is not uniquely determined. Thus, this program is considered incorrect.

| Input | Output | Description |
| --- | --- | --- |
| `5 3` |  | First, you are given integers N and K. |
|  | `? 2 4 1` | You ask a query with (x\_1, x\_2, x\_3) = (2, 4, 1). |
| `0` |  | The response to the query is 0, so the judge returns that value. |
|  | `? 5 3 2` | You ask a query with (x\_1, x\_2, x\_3) = (5, 3, 2). |
| `1` |  | The response to the query is 1, so the judge returns that value. |
|  | `! 1 0 1 1 0` | You print (1, 0, 1, 1, 0) to guess A. Since sequence A is not uniquely determined, the verdict will be WA. |
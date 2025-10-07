Score : 500 points

### Problem Statement

There are N items in a shop, numbered as Item 1, Item 2, \ldots, Item N.  
For each i = 1, 2, \ldots, N, the **regular price** of Item i is A\_i yen. For each item, there is only one in stock.

Takahashi wants M items: Item X\_1, Item X\_2, \ldots, Item X\_M.

He repeats the following until he gets all items he wants.

> Let r be the number of unsold items now.
> Choose an integer j such that 1 \leq j \leq r, and buy the item with the j-th smallest item number among the unsold items, for its **regular price** plus C\_j yen.

Print the smallest total amount of money needed to get all items Takahashi wants.

Takahashi may also buy items other than the ones he wants.

### Constraints

* 1 \leq M \leq N \leq 5000
* 1 \leq A\_i \leq 10^9
* 1 \leq C\_i \leq 10^9
* 1 \leq X\_1 \lt X\_2 \lt \cdots \lt X\_M \leq N
* All values in the input are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N M
A_1 A_2 \ldots A_N
C_1 C_2 \ldots C_N
X_1 X_2 \ldots X_M
```

### Output

Print the answer.

---

### Sample Input 1

```
5 2
3 1 4 1 5
9 2 6 5 3
3 5
```

### Sample Output 1

```
17
```

Here is a way for Takahashi to get all items he wants with the smallest total amount of money.

* Initially, five items, Items 1, 2, 3, 4, 5, are remaining.
  Choose j = 5 to buy the item with the fifth smallest item number among the remaining, Item 5, for A\_5 + C\_5 = 5 + 3 = 8 yen.
* Then, four items, Items 1, 2, 3, 4, are remaining.
  Choose j = 2 to buy the item with the second smallest item number among the remaining, Item 2, for A\_2 + C\_2 = 1 + 2 = 3 yen.
* Then, three items, Items 1, 3, 4, are remaining.
  Choose j = 2 to buy the item with the second smallest item number among the remaining, Item 3, for A\_3 + C\_2 = 4 + 2 = 6 yen.

Now, Takahashi has all items he wants, Items 3 and 5, (along with Item 2, which is not wanted) for a total cost of 8 + 3 + 6 = 17 yen, the minimum possible.

---

### Sample Input 2

```
20 8
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62
32 38 84 49 93 53 26 13 25 2 76 32 42 34 18 77 14 67 88 12
1 3 4 5 8 14 16 20
```

### Sample Output 2

```
533
```
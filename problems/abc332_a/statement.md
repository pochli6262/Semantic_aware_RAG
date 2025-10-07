Score : 100 points

### Problem Statement

AtCoder Inc. sells merchandise through its [online shop](https://suzuri.jp/AtCoder/home).

Takahashi has decided to purchase N types of products from there.  
For each integer i from 1 to N, the i-th type of product has a price of P\_i yen each, and he will buy Q\_i of this.

Additionally, he must pay a shipping fee.  
The shipping fee is 0 yen if the total price of the products purchased is S yen or above, and K yen otherwise.

He will pay the total price of the products purchased plus the shipping fee.  
Calculate the amount he will pay.

### Constraints

* 1\leq N\leq 100
* 1\leq S\leq 10000
* 1\leq K\leq 10000
* 1\leq P\_i\leq 10000
* 1\leq Q\_i\leq 100
* All input values are integers.

---

### Input

The input is given from Standard Input in the following format:

```
N S K
P_1 Q_1
P_2 Q_2
\vdots
P_N Q_N
```

### Output

Print the amount Takahashi will pay for online shopping.

---

### Sample Input 1

```
2 2000 500
1000 1
100 6
```

### Sample Output 1

```
2100
```

Takahashi buys one product for 1000 yen and six products for 100 yen each.  
Thus, the total price of the products is 1000\times 1+100\times 6=1600 yen.  
Since the total amount for the products is less than 2000 yen, the shipping fee will be 500 yen.  
Therefore, the amount Takahashi will pay is 1600+500=2100 yen.

---

### Sample Input 2

```
3 2000 500
1000 1
100 6
5000 1
```

### Sample Output 2

```
6600
```

The total price of the products is 1000\times 1+100\times 6+5000\times 1=6600 yen.  
Since the total amount for the products is not less than 2000 yen, the shipping fee will be 0 yen.  
Therefore, the amount Takahashi will pay is 6600+0=6600 yen.

---

### Sample Input 3

```
2 2000 500
1000 1
1000 1
```

### Sample Output 3

```
2000
```

There may be multiple products with the same price per item.
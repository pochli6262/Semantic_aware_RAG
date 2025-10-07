A = ["RGB","GBR","BRG"]

S = input()
T = input()
print('Yes' if (S in A and T in A) or (S not in A and T not in A) else 'No')
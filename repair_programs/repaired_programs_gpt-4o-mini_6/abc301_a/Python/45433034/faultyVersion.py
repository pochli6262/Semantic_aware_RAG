N = int(input())
S = list(input())
T=0
A=0
for i in range(N):
   if(S[i] == 'T'):T+=1
   elif(S[i] == 'A'):A+=1
   print(f'A:{A},T:{T}')

if T > A:
    print('T')
elif A > T:
    print('A')
else:
    print('T')
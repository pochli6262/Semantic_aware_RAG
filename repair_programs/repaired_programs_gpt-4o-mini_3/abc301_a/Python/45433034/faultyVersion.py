N = int(input())
S = list(input())
T=0
A=0
for i in range(N):
   if(S[i] == 'T'):
       T+=1
   elif(S[i] == 'A'):
       A+=1
   print(f'A:{A},T:{T}')

if(N % 2 == 0):
   if(T>A):
       print('T')
   else:
       print('A')
else:
   print(S[N-1])

if A >= (N/2 + 1):
   print('A')
elif T >= (N/2 + 1):
   print('T')
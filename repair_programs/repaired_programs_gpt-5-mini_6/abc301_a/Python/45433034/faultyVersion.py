N = int(input())
S = list(input())
T=0
A=0
for i in range(N):
   if(i == N-1):
       if(N % 2 == 0):
           if(T>A):print('T')
           else:print('A')
       else:
            print('T' if T + (1 if S[i] == 'T' else 0) > A + (1 if S[i] == 'A' else 0) else 'A')
   if(S[i] == 'T'):T+=1
   elif(S[i] == 'A'):A+=1
   print(f'A:{A},T:{T}')
   if(A>=(N/2+1)):
        print('A')
        break
   elif(T>=(N/2+1)):
        print('T')
        break
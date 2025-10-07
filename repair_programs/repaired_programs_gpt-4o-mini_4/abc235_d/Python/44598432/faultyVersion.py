from queue import Queue
a,N=map(int,input().split())
def rot(N):
    M=str(N)
    return int(M[1:]+M[0])
d=[10**3]*(N+1)
d[1]=0
q=Queue()
q.put(1)
while not q.empty():
    M=q.get()
    if M==N:
        break
    if M*a <= N and d[M*a]>d[M]+1:
        d[M*a]=d[M]+1
        q.put(M*a)
    if M >= 10 and M%10 != 0:
        r=rot(M)
        if d[r]>d[M]+1:
            d[r]=d[M]+1
            q.put(r)
print(d[N] if d[N]!=10**3 else -1)
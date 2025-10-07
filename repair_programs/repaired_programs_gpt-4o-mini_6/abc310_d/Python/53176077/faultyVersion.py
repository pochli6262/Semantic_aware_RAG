N,T,M=map(int,input().split())
hate=set()

for _ in range(M):
    a,b=map(int,input().split())
    hate.add((a,b))
    hate.add((b,a))
    

def f(now):
    if now==N:
        return 1 if len(teams)==T else 0

    ans=0
    
    for i in range(len(teams)):
        if len(teams[i])>0:
            for t in teams[i]:
                if (now,t) in hate:
                    break
            else:
                teams[i].add(now)
                ans+=f(now+1)
                teams[i].remove(now)
    
    if len(teams)<T:
        teams.append(set([now]))
        ans+=f(now+1)
        teams.pop()
        
    return ans

teams=[]
print(f(0))
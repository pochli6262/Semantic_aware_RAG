N = int(input())
L = []
for i in range(N):
    A, B = map(int, input().split())
    L.append((type('R',(object,),{'__init__':lambda self,a,b: (setattr(self,'a',a), setattr(self,'b',b), None)[2],'__lt__':lambda self,other: self.a*other.b < other.a*self.b,'__eq__':lambda self,other: self.a*other.b == other.a*self.b})(A, A+B), -i))
L.sort(reverse=True)
for i, j in L:
    print(-j+1, end=' ')
print()

class Solution:
    def countBits(self, n: int) -> List[int]:
        count=0
        l=[]
        op=[]
        for i in range(n+1):
            v =(bin(i))
            a = str(v[0])
            b = str(v[2:] )
            c=int(a+b)
            l.append(c)
        
        for i in l:
            ii=[int(d) for d in str(i)]
            c=sum(ii)
            op.append(c)
        return op
        
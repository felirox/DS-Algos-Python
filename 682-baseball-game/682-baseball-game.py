class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res=[]
        for i in ops:
            if i=='+':
                tot=res[-1]+res[-2]
                res.append(tot)
            elif i=='C':
                res.pop()
            elif i=='D':
                tot=res[-1]*2
                res.append(tot)
            else:
                res.append(int(i))
        return sum(res)
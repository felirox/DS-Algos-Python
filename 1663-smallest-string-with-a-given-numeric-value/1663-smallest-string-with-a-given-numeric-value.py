class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        op=['a']*n
        k=k-n
        i=n-1
        while k:
            k+=1
            if k/26>=1:
                op[i]='z'
                i-=1
                k=k-26
            else:
                op[i]=chr(k+96)
                k=0
        return ''.join(op)
            
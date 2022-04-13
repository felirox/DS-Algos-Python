class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        op=[[0]*n for _ in range(n)]
        r,c=0,0
        riter=0
        citer=1
        for k in range(n*n):
            op[r][c]=k+1
            if op[(r+riter)%n][(c+citer)%n]:
                riter,citer=citer,-riter
            r+=riter
            c+=citer
        return op
        # for i in range(n**2):
        #     if count==n:
                
        
        
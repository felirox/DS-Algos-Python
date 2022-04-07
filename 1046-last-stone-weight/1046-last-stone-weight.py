class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        count=0
        while len(stones)>1:
            stones.sort()
            print(stones)
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1]!=stones[-2]:
                res=stones[-1]-stones[-2]
                stones.pop()
                stones.pop()            
                stones.append(res)
        if stones:
            return (stones[0])
        else:
            return 0
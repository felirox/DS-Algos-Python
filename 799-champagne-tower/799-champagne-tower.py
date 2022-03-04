class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        topLayer=[poured]
        for i in range(query_row):
            nextLayer=[0]*(len(topLayer)+1)
            for j in range(len(topLayer)):
                excess=(topLayer[j]-1)/2
                if excess>0:
                    nextLayer[j]+=excess
                    nextLayer[j+1]+=excess
            topLayer=nextLayer
        return min(1,(topLayer[query_glass]))
            
        
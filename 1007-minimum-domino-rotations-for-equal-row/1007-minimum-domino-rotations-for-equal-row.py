class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topchange=0
        bottomchange=0
        tot=tops+bottoms
        maxx=max(set(tot),key=tot.count)
        for i in range(len(tops)):
            if tops[i]==maxx and bottoms[i]==maxx:
                continue                    
            elif tops[i]==maxx:
                topchange+=1
            elif bottoms[i]==maxx:
                bottomchange+=1
            else:
                return -1
        return min(topchange,bottomchange)
            
        
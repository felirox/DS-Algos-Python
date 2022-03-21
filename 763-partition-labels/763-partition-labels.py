
class Solution: 
    
    def partitionLabels(self, s: str) -> List[int]:
        last={ c:i for i,c in enumerate(s)}
        op=[]
        cut=0
        skip=0
        for i,c in enumerate(s):
            cut=max(cut,last[c])
            if cut ==i:
                op.append(i+1-skip)
                skip=i+1
        return op